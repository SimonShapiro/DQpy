import pandas

def CustomRule(rule_id:str, rule_desc:str, fn):
    def rule(row:dict, selector:str, value, parameters=None, id_by=None):  #
        passed = fn(row, selector, value, parameters)
        res = {
            "RuleID": rule_id,
            "RuleDescription": rule_desc,
            "AttributeTested": selector,
            "ValueTested": value,
            "Result": "Passed" if passed else "Failed",
        }
        if not id_by:
            res.update(row)
        else:
            # Idiom to select a sub-set from a dictionary
            # {k: bigdict[k] for k in bigdict.keys() & {'l', 'm', 'n'}}
            res.update({k: row[k] for k in row.keys() & id_by})
        return res
    return rule


def convert_to_type(value:str, value_type:str):
    # Returns a converted value or None
    converters = {
        "string": lambda x: str(x),
        "float": lambda x: float(x),
        "integer": lambda x: int(x),
        "boolean": lambda x: bool(x)
    }
    try:
        value = converters[value_type](value)
    except:
        value = None
    return value


def test_row(row:dict, rule_set, id_by:list=None, verbose=False):  # Test a row for all rules in a ruleset
    results = []
    for attr, attr_rules in rule_set.items():
        # Test and cast types here
        value = convert_to_type(row[attr], attr_rules["type"])
        if value == None:
            r = CustomRule("Type Error", "Test data type conversion", lambda w, x, y, z: False)  # create failing rule to use results
            results.append((r(row, attr, row[attr], parameters=None, id_by=id_by)))
        else:
            if "dq rules" in attr_rules.keys():
                for rrule in attr_rules["dq rules"]:
                    rule = rrule["rule"]
                    results.append(rule(row, attr, value,
                                        parameters=None if "parameters" not in rrule.keys() else rrule["parameters"],
                                        id_by=id_by))
#    print(results)
    results = list(filter(lambda r: r["Result"] == "Failed", results)) if not verbose else results
    return results  # An array of results


class CSV_Panda_Memory_Store:
    def __init__(self):
        self.store = {}

    def _add_to_store(self, filename, sep=",", index_col=None):
        if filename not in self.store:
            self.store[filename] = pandas.DataFrame.from_csv(filename, sep=sep, index_col=index_col)

    def lookup_in_csv_store(self, row, selector, value, parameters):
        file_name = parameters["file"]
        self._add_to_store(file_name, sep=",", index_col=None) # do noting if it is already there
        search_col = parameters["col"]
        if not pandas.isnull(value):
            passed = value in self.store[file_name][search_col].unique()
        else:
            passed = False
        return passed
