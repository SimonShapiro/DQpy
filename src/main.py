from src import ledger_sdi_ruleset
from lib.DQpy import test_row
import csv

input_filenm = "/Users/simonshapiro/DQpy/data/enhanced.ledger.sdi.log"
output_filenm = "/Users/simonshapiro/DQpy/data/enhanced.ledger.dq.csv"
with open(output_filenm, "w") as output_file:
    with open(input_filenm, "r") as input_file:
        reader = csv.DictReader(input_file, delimiter='|')
        first_read = True
        for row in reader:
    #        print(row)
            result = test_row(row, ledger_sdi_ruleset.rule_set, verbose=False)
    #        print(result)
            if result:
                if first_read:
                    header = result[0].keys()
                    writer = csv.DictWriter(output_file, delimiter=',', fieldnames=header)
                    writer.writeheader()
                    first_read = False
                writer.writerows(result)
