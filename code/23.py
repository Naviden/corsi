# Python code to calculate completeness measures based on the provided dataset

import pandas as pd

# Load the dataset
df = pd.read_csv('/mnt/data/completeness_issues_dataset.csv')

# Define the functions to calculate the different completeness measures

# Schema Completeness: checks if all expected columns are present in the dataframe
def calculate_schema_completeness(df, expected_columns):
    actual_columns = df.columns.tolist()
    missing_columns = [col for col in expected_columns if col not in actual_columns]
    completeness_ratio = (len(actual_columns) / len(expected_columns)) * 100
    return completeness_ratio, missing_columns

# Column Completeness: checks for the presence of null values in each column
def calculate_column_completeness(df):
    completeness_dict = {}
    for column in df.columns:
        completeness_dict[column] = (df[column].count() / len(df)) * 100
    return completeness_dict

# Population Completeness: for this, we would need a reference population to compare against.
# Since we don't have that, we'll consider 'phone_number' and 'email' as required fields for the sake of example
def calculate_population_completeness(df, population_fields):
    completeness_dict = {}
    for field in population_fields:
        completeness_dict[field] = (df[field].count() / len(df)) * 100
    return completeness_dict

# Assuming a fully complete schema would require the following fields:
expected_columns = ['id', 'first_name', 'last_name', 'dob', 'city', 'state', 'country', 'phone_number', 'email']

# Calculate completeness measures
schema_completeness_ratio, missing_columns = calculate_schema_completeness(df, expected_columns)
column_completeness_dict = calculate_column_completeness(df)
population_fields = ['phone_number', 'email']
population_completeness_dict = calculate_population_completeness(df, population_fields)

(schema_completeness_ratio, missing_columns), column_completeness_dict, population_completeness_dict
