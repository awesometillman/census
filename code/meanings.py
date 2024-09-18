#!/usr/bin/env python

"""Creates a dataframe containing the meanings of the category
codes for each category in the given dataset, then saves the
dataframe to 'Meanings.csv' in the data folder.
"""
import pandas as pd

meanings = pd.DataFrame(columns = ["Title", "Dictionary"])

meanings.loc["RESIDENCE_TYPE"] = ["Residence Type", {
    "C": "Resident in a Communal Establishment",
    "P": "Not resident in a Communal Establishment"
}]
meanings.loc["Family_Composition"] = ["Family Composition", {
    "0": "Not in a family",
    "1": "Married/same-sex civil partnership couple family",
    "2": "Cohabiting couple family",
    "3": "Lone parent family (male head)",
    "4": "Lone parent family (female lead)",
    "5": "Other related family",
    "X": "No code required (residents of a communal establishment)"
}]
meanings.loc["sex"] = ["Sex", {
    "1": "Male",
    "2": "Female"
}]
meanings.loc["age"] = ["Age", {
    "1": "0 to 15",
    "2": "16 to 24",
    "3": "25 to 34",
    "4": "35 to 44",
    "5": "45 to 54",
    "6": "55 to 64",
    "7": "65 to 74",
    "8": "75 and over"
}]
meanings.loc["Marital_Status"] = ["Marital Status", {
    "1": "Single (Never married or never registered a same-sex civil partnership",
    "2": "Married or in a same sex-civil partnership",
    "3": "Separated, but still legally married or still legally in a same-sex civil partnership",
    "4": "Divorced or formerly in a same-sex civil partnership which is now legally dissolved",
    "5": "Widowed or surviving partner from a same-sex civil partnership"
}]
meanings.loc["student"] = ["Student", {
    "1": "Yes",
    "2": "No"
}]
meanings.loc["Country_Of_Birth"] = ["Country Of Birth", {
    "1": "UK",
    "2": "Non UK"
}]
meanings.loc["health"] = ["Health", {
    "1": "Very good health",
    "2": "Good health",
    "3": "Fair health",
    "4": "Bad health",
    "5": "Very bad health"
}]
meanings.loc["Ethnic_Group"] = ["Ethnic Group", {
    "1": "White",
    "2": "Mixed or multiple ethnic group",
    "3": "Asian",
    "4": "African",
    "5": "Caribbean or black",
    "6": "Other ethnic group"
}]
meanings.loc["religion"] = ["Religion", {
    "1": "No religion",
    "2": "Christian",
    "3": "Buddhist",
    "4": "Hindu",
    "5": "Jewish",
    "6": "Muslim",
    "7": "Sikh",
    "8": "Other religion",
    "9": "Not stated"
}]
meanings.loc["Economic_Activity"] = ["Economic Activity", {
    "1": "Economically active: Employed",
    "2": "Economically active: Self-Employed",
    "3": "Economically active: Unemployed",
    "4": "Economically active: Full-time student",
    "5": "Economically inactive: Retired",
    "6": "Economically inactive: Student",
    "7": "Economically inactive: Looking after home or family",
    "8": "Economically inactive: Long-term sick or disabled",
    "9": "Economically inactive: Other",
    "X": "No code required (Aged under 16)"
}]
meanings.loc["Occupation"] = ["Occupation", {
    "1": "Managers, Directors and Senior Officials",
    "2": "Professional Occupations",
    "3": "Associate Professional and Technical Occupations",
    "4": "Administrative and Secretarial Occupations",
    "5": "Skilled Trades Occupations",
    "6": "Caring, Leisure and Other Service Occupations",
    "7": "Sales and Customer Service Occupations",
    "8": "Process, Plant and Machine Operatives",
    "9": "Elementary Occupations",
    "X": "No code required (People aged under 16 and people who have never worked)"
}]
meanings.loc["industry"] = ["Industry", {
    "1": "Agriculture, forestry and fishing",
    "2": "Mining and quarrying; Manufacturing; Electricity, gas, steam and air conditioning system; Water supply",
    "3": "Construction",
    "4": "Wholesale and retail trade; Repair of motor vehicles and motorcycles",
    "5": "Accommodation and food service activities",
    "6": "Transport and storage; Information and communication",
    "7": "Financial and insurance activities",
    "8": "Real estate activities; Professional scientific and technical activities; Administrative and support service activities",
    "9": "Public administration and defence",
    "10": "Education",
    "11": "Human health and social work activities",
    "12": "Arts; entertainment and recreation",
    "13": "Other",
    "X": "No code required (People aged under 16 and people who have never worked)"
}]
meanings.loc["Hours_Worked_Per_Week"] = ["Hours Worked Per Week", {
    "1": "Part-time: 15 or less hours worked",
    "2": "Part-time: 16 to 30 hours worked",
    "3": "Full-time: 31 to 48 hours worked",
    "4": "Full-time 49 or more hours worked",
    "X": "No code required (People aged under 16 and people not working)"
}]
meanings.loc["Approximate_Social_Grade"] = ["Approximate Social Grade", {
    "1": "AB",
    "2": "C1",
    "3": "C2",
    "4": "DE",
    "X": "No code required ( People aged under 16 and people resident in communal establishments)"
}]

meanings.to_csv("../data/Meanings.csv", index = True)
print("Successfully wrote to Meanings.csv")