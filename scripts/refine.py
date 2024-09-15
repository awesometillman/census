#!/usr/bin/env python

import pandas as pd
import sys

def check_col_names(format, input):
    """Checks that column names of input dataframe match required format.
    
    If any column names don't match, prints error message and returns False.
    Returns True if no mismatches are found.
    """

    col_names_match = True

    for i in range(len(input.columns)):
        if not format["Variable_Name"][i] == input.columns[i]:
            print("Invalid column name: expected", format["Variable_Name"][i], "but got",
                  input.columns[i])
            col_names_match = False

    return col_names_match

def check_col_dtypes(format, input):
    """Checks that data types of input dataframe columns are correct.
    
    If any column is the wrong type, prints error message and returns False.
    Returns True if no columns are the wrong type.
    """

    col_dtypes_match = True

    for i in range(len(input.columns)):
        if not format["Data_Type"][i] == input.dtypes.iloc[i]:
            print("Invalid data type of", format["Variable_Name"][i] + ": expected", 
                  format["Data_Type"][i], "but got", input.dtypes.iloc[i])
            col_dtypes_match = False

    return col_dtypes_match

def remove_bad_rows(format, input):
    """Removes rows which contain invalid entries in at least one column.
    
    Returns a refined version of the input dataframe.
    """

    output = input
    drop_list = []

    for index in range(len(output.columns)):

        if format["Data_Type"][index] == int:
            # Check that entries in every numerical column are within specified range

            column = output[format["Variable_Name"][index]]
            lower = format["Accepted_Vals"][index][0]
            upper = format["Accepted_Vals"][index][1]
            
            for i in range(len(column)):
                entry = column[i]

                if (entry < lower) or (upper < entry):
                    print("Entry out of range in", output.columns[index], "column:")
                    print("(row", str(i) + ")", entry, "not between",
                          lower, "and", upper)
                    drop_list.append(i)
        else:
            # Check that entries in every categorical column are on the specified list

            column = output[format["Variable_Name"][index]]

            for i in range(len(column)):
                entry = column[i]

                if not entry in format["Accepted_Vals"][index]:
                    print("Invalid entry in", output.columns[index], "column:")
                    print("(row", str(i) + ") '" + str(entry) +
                          "' not in list", format["Accepted_Vals"][index])
                    drop_list.append(i)
    
    output = output.drop(drop_list)
                    
    return output

def main():
    """Checks and refines input data.
    
    If input data has correct column names and data types, a refined
    version of the input dataframe is saved to a separate csv file
    called 'Refined_dataset.csv'.
    """

    # Create dataframe containing the required format for input data.
    # This information is taken from 'Microdata_Teach_File_Overview.docx'.
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

    # Perform checks on input data, and only refine if both checks pass
    if check_col_names(format_df, input_df):
        print("All column names match.")

        if check_col_dtypes(format_df, input_df):
            print("All data types match.")

            # Refine dataset by removing invalid data and duplicate rows
            print("Rows before removing invalid entries:", input_df.shape[0])
            output_df = remove_bad_rows(format_df, input_df)
            print("Rows after removing invalid entries:", output_df.shape[0])

            print("Rows before deleting duplicates:", output_df.shape[0])
            output_df = output_df.drop_duplicates()
            print("Rows after deleting duplicates:", output_df.shape[0])

            # Output refined dataset to a csv file to be used later
            output_df.to_csv("../data/Refined_dataset.csv", index = False)
            print("Successfully wrote to Refined_dataset.csv")

if __name__ == "__main__":
    print("script name is", sys.argv[0])
    if (len(sys.argv) == 2):
        main()