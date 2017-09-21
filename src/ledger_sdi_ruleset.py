from rules.dq_rules import *

# Ruleset for the ledger sdi


rule_set = {
    "RecordType": {
        "type": "string",
        "dq rules": [
            {"rule": Rule_001},
            {"rule": CR_001, "parameters":{"pattern": "^B"}},
        ]
    },
    "SourceSystemId": {
        "type": "string",
        "dq rules": [
            {"rule": Rule_001},
            {"rule": CR_004, "parameters":{"list":["HUBAU"]}},
        ]
    },
    "LegalEntity": {
        "type": "string",
        "dq rules": [
            {"rule": Rule_001},
            {"rule": CR_004, "parameters":{"list":["'4435'"]}},  #This should be a call to an authatative source
            {"rule": CR_005, "parameters":{"file":"/Users/simonshapiro/DQpy/data/company_codes.csv",
                                    "col": "SaracenCode"}
             },  #This should be a call to an authatative source
        ]
    },
    "GLKey": {
        "type": "string",
        "dq rules": [
            {"rule":Rule_001},
            {"rule":CR_001, "parameters": {"pattern": "[0-9]{5}-[A,L]"}}
        ]
    },
    "GLBalance": {
        "type": "float",
        "dq rules": [
            {"rule": CR_003} #Number sign should follow last character of GLKey
        ]
    },
    "BankingORTradingBook": {
        "type": "string",
        "dq rules": [
            {"rule":Rule_001},
            {"rule":CR_004, "parameters":{"list":["B", "T"]}},
        ]
    },
    "GroupReconciliationKey": {
        "type": "string",
        "dq rules": [
            {"rule":Rule_001},
            {"rule":CR_001, "parameters":{"pattern":"[A-Z]{2}[0-9]{5}"}},
        ]
    },
    "GLBalanceCurrencyCode": {
        "type": "string",
        "dq rules": [
            {"rule":Rule_001, "parameters":{}},
            {"rule":CR_005, "parameters": {
                                "file": "/Users/simonshapiro/DQpy/data/currency_codes.csv",
                                "col": "Alphabetic Code"
                            }
             }
        ]
    },
    "ReportingBalanceCurrencyCode": {
        "type": "string",
        "dq rules": [
            {"rule":Rule_001, "parameters":{}},
             {"rule": CR_005, "parameters": {
                 "file": "/Users/simonshapiro/DQpy/data/currency_codes.csv",
                 "col": "Alphabetic Code"
                }
            }
        ]
    },
    "GLBalanceInReportingCCY": {
        "type": "float",
    }
}