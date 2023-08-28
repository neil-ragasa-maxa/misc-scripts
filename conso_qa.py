import pandas as pd
import numpy as np
import math
import inputs
import variance


df = pd.read_excel(inputs.file_name, sheet_name='Export')

# cleaning
df.iloc[:, 1] = df.iloc[:, 1].str.strip()
df = df.fillna(0)
df.iloc[:, :] = df.iloc[:, :].astype(str)

# removes % and divide by 100
df.iloc[:, 2:8]=df.iloc[:, 2:8].apply(lambda x:
                           (x.str.replace('%', '')).astype(float)/100
                             if x.str.contains('%', na=False).any() else x, axis=1)

# # transform column 3 to 9 to float
df.iloc[:, 2:8] = df.iloc[:, 2:8].astype(float) # can't round it here because 
                                                # calculations will be wrong 
                                                # and won't be equal to expected answer

columns = {2: 'c', 3: 'd', 6:'g'}
cells = inputs.cells
for column in columns:
    for department in cells:
        for category in cells[department]:
            numerator = 0
            denominator = 0
            category_dict = cells[department][category]
            if "positive" in category_dict["num"]:
                for index in category_dict["num"]["positive"]:
                    numerator += df.iloc[index-2, column]
            else: pass
            if "negative" in category_dict["num"]:
                for index in category_dict["num"]["negative"]:
                    numerator -= df.iloc[index-2, column]
            else: pass
            if "denum" in category_dict:
                for index in category_dict["denum"]["positive"]:
                    denominator += df.iloc[index-2, column]
            else:
                denominator = 1
            calculation = round(numerator / denominator if denominator else 0, 3)
            table_value_index = cells[department][category]["ans"]
            table_value = round(df.iloc[table_value_index-2, column], 3)
            if math.isclose(table_value, calculation, abs_tol=inputs.tolerance):
                pass
            else:
                print("\nDepartment -> {department}".format(department=department))
                print("Category -> {category}".format(category=category))
                print("\tCalculation = {calculation}".format(calculation=calculation))
                print("\tExpected Answer = {answer}".format(answer=table_value))
                print("\t\tCell: {cell}{row}".format(cell=columns[column], row=table_value_index))
                # print("numerator = {numerator}".format(numerator=category_dict["num"]))
                # print("denominator = {denominator}".format(denominator=category_dict["denum"]))
                print("\n")

substraction_pairs = inputs.substraction_pairs
for key in substraction_pairs:
    variance.variance_dollar(substraction_pairs[key][0], substraction_pairs[key][1], key, substraction_pairs[key][2], df)