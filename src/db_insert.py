import psycopg2

conn = psycopg2.connect(host="localhost", dbname="voterdata", port=5433, user="postgres",
password="titan") # this a connection string between the code and the database

print(type(conn)) # checks if the connection string works

cursor = conn.cursor() # the cursor works as a middleman between the code and database and fetches the data virtually

# INSERT
cursor.execute("INSERT INTO voter VALUES (107, 'Holden', 'E', 'Caulfield', 1965, '571 Times Street', 1)")
cursor.execute("SELECT * FROM voter WHERE voter_firstname = 'Holden'") # selects row that was inserted
print("Inserted New Voter =", cursor.fetchall()) # fetches all rows with Holden as the voter_firstname (there is only one)