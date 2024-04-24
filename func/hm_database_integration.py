import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Execute a SQL query to retrieve data from a table
cur.execute("SELECT * FROM mytable")

# Fetch all the rows returned by the query
rows = cur.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
