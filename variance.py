import math
import pandas as pd
import inputs
def variance_dollar(positive_column_index: int, negative_column_index: int, column_index: int, column_variances_dollar: dict, df: pd.DataFrame):
    df_copy = df.copy()
    df_copy["calculation"] = df_copy.iloc[:, positive_column_index] - df_copy.iloc[:, negative_column_index]
    unmatched_variance_dollar = df_copy[df_copy.apply(lambda x: not math.isclose(x["calculation"], x[column_index], abs_tol=inputs.tolerance), axis=1)]

    print(pd.concat([
        unmatched_variance_dollar[["Département", "Description", "calculation"]],
        unmatched_variance_dollar.iloc[:, [positive_column_index, negative_column_index, column_index]],
        ],
        axis=1))