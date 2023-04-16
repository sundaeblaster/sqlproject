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

# SELECT
cursor.execute('SELECT candidate_firstname FROM candidate') # pulls rows from a particular column within a table
print("fetchone =", cursor.fetchone()) # fetches one row
print("fetchall =", cursor.fetchall()) # fetches all rows
cursor.execute('SELECT candidate_firstname FROM candidate') # the cursor must be updated again so it has all the rows to work with again
print("fetchmany(2) =", cursor.fetchmany(size = 2)) # fetches two rows


