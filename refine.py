#!/usr/bin/env python

#refine the dataset:

#    develop a procedure to check that the data match expected format, remove duplicates, and perform further refinement. This procedure should ensure that:

#        1. the values of variables are of the expected format (numbers, strings, etc.);

#        2. the values of variables are admissible (e.g. are within a given range or are from the list of admissible values);

#    in case of any inconsistencies and/or duplicates found, produce new file with refined data to be used in the subsequent analysis;

#    this step must be automated to the point when it can be run with a single shell command to call an executable Python script specifying necessary argument(s);

#    the refinement process should be documented (e.g. using comments in the code) in case one may need to modify and re-run it (although it’s not necessary to repeat it each time while re-running the analysis),

import pandas as pd

vars_info = [["Record_Number", int, [1, 63388]],
             ["Region", object, ["S92000003"]],
             ["RESIDENCY_TYPE", object, ["C", "P"]],
             ["Family_Composition", object, ["0", "1", "2", "3", "4", "5", "X"]],
             ["sex", int, [1, 2]],
             ["age", int, [1, 8]],
             ["Marital_Status", int, [1, 5]],
             ["student", int, [1, 2]],
             ["health", int, [1, 5]],
             ["Ethnic_Group", int, [1, 6]],
             ["religion", int, [1, 9]],
             ["Economic_Activity", object, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]],
             ["Occupation", object, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]],
             ["industry", object, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "X"]],
             ["Hours_Worked_Per_Week", object, ["1", "2", "3", "4", "X"]],
             ["Approximage_Social_Grade", object, ["1", "2", "3", "4", "X"]]]

format_df = pd.DataFrame(vars_info, columns = ["Variable Name", "Data Type", "Accepted Vals"])

print(format_df)