#!/usr/bin/env python

#refine the dataset:

#    develop a procedure to check that the data match expected format, remove duplicates, and perform further refinement. This procedure should ensure that:

#        1. the values of variables are of the expected format (numbers, strings, etc.);

#        2. the values of variables are admissible (e.g. are within a given range or are from the list of admissible values);

#    in case of any inconsistencies and/or duplicates found, produce new file with refined data to be used in the subsequent analysis;

#    this step must be automated to the point when it can be run with a single shell command to call an executable Python script specifying necessary argument(s);

#    the refinement process should be documented (e.g. using comments in the code) in case one may need to modify and re-run it (although it’s not necessary to repeat it each time while re-running the analysis),

import pandas as pd
import sys

def check_col_names(format, input):
    col_names_match = True

    for i in range(len(input.columns)):
        if not format["Variable_Name"][i] == input.columns[i]:
            print("Invalid column name: expected", format["Variable_Name"][i], "but got",
                  input.columns[i])
            col_names_match = False

    return col_names_match

def check_col_dtypes(format, input):
    col_dtypes_match = True

    for i in range(len(input.columns)):
        if not format["Data_Type"][i] == input.dtypes.iloc[i]:
            print("Invalid data type of", format["Variable_Name"][i] + ": expected", 
                  format["Data_Type"][i], "but got", input.dtypes.iloc[i])
            col_dtypes_match = False

    return col_dtypes_match

def main():
    vars_info = [["Record_Number", int, [1, 63388]],
                ["Region", object, ["S92000003"]],
                ["RESIDENCE_TYPE", object, ["C", "P"]],
                ["Family_Composition", object, ["0", "1", "2", "3", "4", "5", "X"]],
                ["sex", int, [1, 2]],
                ["age", int, [1, 8]],
                ["Marital_Status", int, [1, 5]],
                ["student", int, [1, 2]],
                ["Country_Of_Birth", int, [1, 2]],
                ["health", int, [1, 5]],
                ["Ethnic_Group", int, [1, 6]],
                ["religion", int, [1, 9]],
                ["Economic_Activity", object, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]],
                ["Occupation", object, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]],
                ["industry", object, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "X"]],
                ["Hours_Worked_Per_Week", object, ["1", "2", "3", "4", "X"]],
                ["Approximate_Social_Grade", object, ["1", "2", "3", "4", "X"]]]

    format_df = pd.DataFrame(vars_info, columns = ["Variable_Name", "Data_Type", "Accepted_Vals"])
    input_df = pd.read_csv(sys.argv[1])

    if check_col_names(format_df, input_df):
        print("All column names match.")

        if check_col_dtypes(format_df, input_df):
            print("All data types match.")

if __name__ == "__main__":
    print("script name is", sys.argv[0])
    if (len(sys.argv) == 2):
        main()