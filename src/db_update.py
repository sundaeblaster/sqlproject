import psycopg2
from configparser import ConfigParser

parser = ConfigParser()
parser.read("/Users/sameer/code/python/dbcode/creds.ini")
pgcreds = {}
if parser.has_section("pgdb"):
    items = parser.items("pgdb")
    for item in items:
        pgcreds[item[0]] = item[1]

conn = psycopg2.connect(**pgcreds) # this a connection string between the code and the database

print(type(conn)) # checks if the connection string works

cursor = conn.cursor() # the cursor works as a middleman between the code and database and fetches the data virtually

# UPDATE
cursor.execute("UPDATE candidate SET candidate_party = 'Libertarian' WHERE candidate_id = 1")
cursor.execute("SELECT * FROM candidate WHERE candidate_id = 1")
print("Update Candidate Party To Libertarian:", cursor.fetchall())