file_name = "data.xlsx"
tolerance = 0.005 # conditional tolerance
cells = {
    "new_truck":{
        # divisions
        "profit_per_truck":{
            "num":{
                "positive":[4],
            },
            "denum":{
                "positive":[2],
            },
            "ans":5,
        },
        "profit_percent":{
            "num":{
                "positive":[4],
            },
            "denum":{
                "positive":[3]
            },
            "ans":6,
        },
        "var_expense_profit_percent": {
            "num":{
                "positive":[7],
            },
            "denum":{
                "positive":[4],
            },
            "ans":8,
        },
        "after_control_expense_profit_percent": {
            "num":{
                "positive":[10],
            },
            "denum":{
                "positive":[4],
            },
            "ans":11,
        },
        "bai_percent":{
            "num":{
                "positive":[14],
                "negative":[12],
            },
            "denum":{
                "positive":[4],
            },
            "ans":15,
        },
        # sums
        "after_control_expense_profit":{
            "num":{
                "positive":[4],
                "negative":[7, 9],
            },
            "ans":10,
        },
        "bai_perte":{
            "num":{
                "positive":[10, 12],
                "negative":[13],
            },
            "ans":14,
        }
    },
    "used":{
        # divisions
        "profit_per_truck":{
            "num":{
                "positive":[19],
            },
            "denum":{
                "positive":[17],
            },
            "ans":20,
        },
        "profit_percent":{
            "num":{
                "positive":[19],
            },
            "denum":{
                "positive":[18]
            },
            "ans":21,
        },
        "var_expense_profit_percent": {
            "num":{
                "positive":[22],
            },
            "denum":{
                "positive":[19],
            },
            "ans":23,
        },
        "after_control_expense_profit_percent": {
            "num":{
                "positive":[25],
            },
            "denum":{
                "positive":[19],
            },
            "ans":26,
        },
        "bai_percent":{
            "num":{
                "positive":[29],
                "negative":[27],
            },
            "denum":{
                "positive":[19],
            },
            "ans":30,
        },
        # sums
        "after_control_expense_profit":{
            "num":{
                "positive":[19],
                "negative":[22, 24],
            },
            "ans":25,
        },
        "bai_perte":{
            "num":{
                "positive":[25, 27],
                "negative":[28],
            },
            "ans":29,
        }
    },
    "service":{
        # divisions
        "profit_percent_hours":{
            "num":{
                "positive":[33],
            },
            "denum":{
                "positive":[32],
            },
            "ans":34,
        },
        "profit_percent_parts":{
            "num":{
                "positive":[36],
            },
            "denum":{
                "positive":[35],
            },
            "ans":37,
        },
        "var_expense_profit_percent": {
            "num":{
                "positive":[38],
            },
            "denum":{
                "positive":[32, 35],
            },
            "ans":39,
        },
        "after_control_expense_profit_percent": {
            "num":{
                "positive":[41],
            },
            "denum":{
                "positive":[32, 35],
            },
            "ans":42,
        },
        "bai_percent": {
            "num":{
                "positive":[44],
            },
            "denum":{
                "positive":[32, 35],
            },
            "ans":45,
        },
        # sums
        "after_control_expense_profit":{
            "num":{
                "positive":[33, 36],
                "negative":[38, 40],
            },
            "ans":41,
        },
        "bai_perte":{
            "num":{
                "positive":[41],
                "negative":[43],
            },
            "ans":44,
        }

    },
    "body":{
        # divisions
        "profit_percent":{
            "num":{
                "positive":[48],
            },
            "denum":{
                "positive":[47],
            },
            "ans":49,
        },
        "var_expense_profit_percent": {
            "num":{
                "positive":[50],
            },
            "denum":{
                "positive":[47],
            },
            "ans":51,
        },
        "after_control_expense_profit_percent": {
            "num":{
                "positive":[53],
            },
            "denum":{
                "positive":[47],
            },
            "ans":54,
        },
        "bai_percent": {
            "num":{
                "positive":[56],
            },
            "denum":{
                "positive":[47],
            },
            "ans":57,
        },
        # sums
        "after_control_expense_profit":{
            "num":{
                "positive":[48],
                "negative":[50, 52],
            },
            "ans":53,
        },
        "bai_perte":{
            "num":{
                "positive":[53],
                "negative":[55],
            },
            "ans":56,
        }
    },
    "parts":{
        # divisions
        "profit_percent":{
            "num":{
                "positive":[60],
            },
            "denum":{
                "positive":[59],
            },
            "ans":61,
        },
        "profit_percent_interco":{
            "num":{
                "positive":[63],
            },
            "denum":{
                "positive":[62],
            },
            "ans":64,
        },
        "var_expense_profit_percent": {
            "num":{
                "positive":[65],
            },
            "denum":{
                "positive":[59, 62],
            },
            "ans":66,
        },
        "after_control_expense_profit_percent": {
            "num":{
                "positive":[68],
            },
            "denum":{
                "positive":[59, 62],
            },
            "ans":69,
        },
        "bai_percent": {
            "num":{
                "positive":[71],
            },
            "denum":{
                "positive":[59, 62],
            },
            "ans":72,
        },
        # sums
        "after_control_expense_profit":{
            "num":{
                "positive":[60, 63],
                "negative":[65, 67],
            },
            "ans":68,
        },
        "bai_perte":{
            "num":{
                "positive":[68],
                "negative":[70],
            },
            "ans":71,
        }
    }
}
# table_value_index:[positive_column, negative_column, table_value_excel_letter]
substraction_pairs = {
    4:[2, 3, "e"],
    7:[2, 6, "h"]
    }