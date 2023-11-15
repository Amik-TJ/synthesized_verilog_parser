lib_dictionary = {
    "ADDFHX1": {
        "pins": {
            "A" : {
                "direction": "input",
                "capacitance": 0.006053,
            },
            "B" : {
                "direction": "input",
                "capacitance": 0.013876,
            },
            "CI" : {
                "direction": "input",
                "capacitance": 0.004189,
            },
            "S" : {
                "direction": "output",
                "capacitance": 0.0,
                "function" : "(A ^ B ^ CI)",
                "max_capacitance" : 0.311500,
            },
            "CO" : {
                "direction": "output",
                "capacitance": 0.0,
                "function" : "(((A ^ B) CI) | (A B))",
                "max_capacitance" : 0.311500,
            }
        },
        "area" : 76.507200,
        "cell_leakage_power" : 4104.182520
    },
    "ADDFHX2": {
        "pins": {
            "A" : {
                "direction": "input",
                "capacitance": 0.011305,
            },
            "B" : {
                "direction": "input",
                "capacitance": 0.025038,
            },
            "CI" : {
                "direction": "input",
                "capacitance": 0.007735,
            },
            "S" : {
                "direction": "output",
                "capacitance": 0.0,
                "function" : "(A ^ B ^ CI)",
                "max_capacitance" : 0.623000,
            },
            "CO" : {
                "direction": "output",
                "capacitance": 0.0,
                "function" : "(((A ^ B) CI) | (A B))",
                "max_capacitance" : 0.623000,
            }
        },
        "area" : 113.097600,
        "cell_leakage_power" : 7522.904160
    }
}