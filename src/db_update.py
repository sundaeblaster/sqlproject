import psycopg2

conn = psycopg2.connect(host="localhost", dbname="voterdata", port=5433, user="postgres",
password="titan") # this a connection string between the code and the database

print(type(conn)) # checks if the connection string works

cursor = conn.cursor() # the cursor works as a middleman between the code and database and fetches the data virtually

# UPDATE
cursor.execute("UPDATE candidate SET candidate_party = 'Libertarian' WHERE candidate_id = 1")
cursor.execute("SELECT * FROM candidate WHERE candidate_id = 1")
print("Update Candidate Party To Libertarian:", cursor.fetchall())