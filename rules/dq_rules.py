from lib.DQpy import *
import re
import pandas


def test_blank(row, selector, value, parameters):
    result = True if value != "" else False
    return result

Rule_001 = CustomRule("Rule_001", "Test for blank", test_blank)


def test_regex(row, selector, value, parameters):
    pattern = parameters["pattern"]
    r = re.compile(pattern)
    result = True if r.match(str(value)) else False
    return result

CR_001 = CustomRule("CR_001", "Test regex", test_regex)


def lookup_in_csv(row, selector, value, parameters):
    # Sets up a data frame for a csv in order to fake a database table
    # !!!! Highly inefficient because it should be an api call to a refdata service
    file_name = parameters["file"]
    data = pandas.DataFrame.from_csv(file_name, sep=",", index_col=None)
    search_col = parameters["col"]
    if not pandas.isnull(value):
        passed = value in list(data[search_col])
    else:
        passed = False
    return passed

CR_002 = CustomRule("CR_002", "Test against reference csv", lookup_in_csv)


def test_balance_conforms_to_GLKey(row, selector, value, parameters):
    gl_key = row["GLKey"]
    if gl_key:
        last_char = gl_key[-1]
        if (last_char == 'L') and (value <= 0.0):
            result = True
        elif (last_char == "A") and (value >= 0.0):
            result = True
        else:
            result = False
    else:
        result = False
    return result

CR_003 = CustomRule("CR_003", "Test for sign of balance in account", test_balance_conforms_to_GLKey)


CR_004 = CustomRule("CR_004", "Test for value in list", lambda row, selector, value, parameters: value in parameters["list"])

csv_store = CSV_Panda_Memory_Store()

CR_005 = CustomRule("CR_005", "Setup and test in with memory csv store", csv_store.lookup_in_csv_store)