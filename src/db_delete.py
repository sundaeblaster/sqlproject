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

# DELETE
cursor.execute("DELETE FROM voter WHERE voter_firstname = 'Holden'")
cursor.execute("SELECT voter_id, voter_firstname FROM voter")
print("All Voters =", cursor.fetchall())