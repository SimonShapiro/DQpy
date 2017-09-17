from src import ledger_sdi_ruleset
from lib.DQpy import test_row
import csv

input_filenm = "/Users/simonshapiro/DQpy/data/enhanced.ledger.sdi.log"
output_filenm = ""
results = []
with open(input_filenm, "r") as input_file:
    reader = csv.DictReader(input_file, delimiter='|')
    for row in reader:
#        print(row)
        result = test_row(row, ledger_sdi_ruleset.rule_set, verbose=False)
#        print(result)
        if result: results.append(result)
print(results)