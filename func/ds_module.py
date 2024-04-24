# ds_module.py

import pandas as pd
import numpy as np

def create_dataframe(data):
    """
    Create a pandas DataFrame from the given data.
    """
    df = pd.DataFrame(data)
    return df

def add_column(df, column_name, column_data):
    """
    Add a new column to the DataFrame.
    """
    df[column_name] = column_data
    return df

def filter_dataframe(df, column_name, filter_value):
    """
    Filter the DataFrame based on a given column and value.
    """
    filtered_df = df[df[column_name] == filter_value]
    return filtered_df

def sort_dataframe(df, column_name, ascending=True):
    """
    Sort the DataFrame based on a given column.
    """
    sorted_df = df.sort_values(column_name, ascending=ascending)
    return sorted_df

def group_dataframe(df, column_name):
    """
    Group the DataFrame based on a given column.
    """
    grouped_df = df.groupby(column_name)
    return grouped_df

def aggregate_dataframe(grouped_df, aggregation_functions):
    """
    Aggregate the DataFrame using the given aggregation functions.
    """
    aggregated_df = grouped_df.agg(aggregation_functions)
    return aggregated_df

def merge_dataframes(df1, df2, on_column):
    """
    Merge two DataFrames based on a common column.
    """
    merged_df = pd.merge(df1, df2, on=on_column)
    return merged_df

# Example usage
data = [
    ["Alice", 25, "Engineer"],
    ["Bob", 30, "Manager"],
    ["Charlie", 22, "Engineer"],
    ["David", 35, "Director"]
]
df = create_dataframe(data)
print("Original DataFrame:")
print(df)

df = add_column(df, "Department", ["IT", "Management", "IT", "Management"])
print("\nDataFrame with Department column:")
print(df)

filtered_df = filter_dataframe(df, "Department", "IT")
print("\nFiltered DataFrame (Department=IT):")
print(filtered_df)

sorted_df = sort_dataframe(df, "Age", ascending=False)
print("\nSorted DataFrame (Age, descending):")
print(sorted_df)

grouped_df = group_dataframe(df, "Department")
print("\nGrouped DataFrame (Department):")
print(grouped_df)

aggregation_functions = {
    "Age": "mean",
    "Name": lambda x: " ".join(x)
}
aggregated_df = aggregate_dataframe(grouped_df, aggregation_functions)
print("\nAggregated DataFrame:")
print(aggregated_df)

merged_df = merge_dataframes(df, aggregated_df, "Department")
print("\nMerged DataFrame:")
print(merged_df)
