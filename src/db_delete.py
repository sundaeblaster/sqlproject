import psycopg2

conn = psycopg2.connect(host="localhost", dbname="voterdata", port=5433, user="postgres",
password="titan") # this a connection string between the code and the database

print(type(conn)) # checks if the connection string works

cursor = conn.cursor() # the cursor works as a middleman between the code and database and fetches the data virtually

# DELETE
cursor.execute("DELETE FROM voter WHERE voter_firstname = 'Holden'")
cursor.execute("SELECT voter_id, voter_firstname FROM voter")
print("All Voters =", cursor.fetchall())