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

# INSERT
cursor.execute("INSERT INTO voter VALUES (107, 'Holden', 'E', 'Caulfield', 1965, '571 Times Street', 1)")
cursor.execute("SELECT * FROM voter WHERE voter_firstname = 'Holden'") # selects row that was inserted
print("Inserted New Voter =", cursor.fetchall()) # fetches all rows with Holden as the voter_firstname (there is only one)