import os
import sys
import time
import random
import com.tableau.hyperapi as hapi

# Define the path to the .hyper file
hyper_file = "path/to/your/file.hyper"

# Define the schema for the table
schema = hapi.TableDefinition(
    hapi.TableName("Extract", "Extract"),
    [
        hapi.TableDefinition.Column("rowID", hapi.SqlType.big_int()),
        hapi.TableDefinition.Column("value", hapi.SqlType.big_int()),
    ],
)

# Create a new HyperProcess instance
with hapi.HyperProcess(telemetry=hapi.Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
    # Connect to the .hyper file
    with hapi.Connection(hyper.endpoint, hyper_file, hapi.CreateMode.CREATE_AND_REPLACE) as connection:
        # Create a new schema in the .hyper file
        connection.catalog.create_schema("Extract")

        # Create a new table in the .hyper file
        connection.catalog.create_table(schema)

        # Insert data into the table using an Inserter
        with hapi.Inserter(connection, schema) as inserter:
            for i in range(1, 101):
                inserter.add_row([i, i])
            inserter.execute()

        # Query data from the table using SQL
        result = connection.execute_query(query="SELECT * FROM Extract.Extract")

        # Print the results
        print("Results:")
        for row in result:
            print(row)

        # Perform parallel processing tasks using Dask
        import dask.dataframe as dd

        # Read the table data into a Dask DataFrame
        df = dd.from_pandas(connection.execute_query(query="SELECT * FROM Extract.Extract"), npartitions=4)

        # Perform some parallel processing tasks on the DataFrame
        df["value"] = df["value"] * 2
        df["rowID"] = df["rowID"] + 100

        # Write the processed data back to the table
        with hapi.Inserter(connection, schema) as inserter:
            for partition in df.partitions:
                for index, row in partition.iterrows():
                    inserter.add_row(list(row))
                inserter.execute()

        # Query the updated data from the table
        result = connection.execute_query(query="SELECT * FROM Extract.Extract")

        # Print the updated results
        print("Updated Results:")
        for row in result:
            print(row)
