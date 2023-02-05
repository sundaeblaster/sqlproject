# Voter Database
##### This database features sample voter and candidate data and the organization of this data into tables. Using pgadmin4, I have created multiple tables to organize the data, and these tables include: voters, candidates, election, result. Listed below are the tables and their purpose in the database.

## Candidates
Columns include, cand_id, cand_fullname, cand_age, cand_party, district

## Voters
Columns include voter_id, voter_fullname, voter_age, voter_address, district

## Election
Columns include voter_id, cand_id, date

## Result
Colmns include result_id, district, winner, cand_id, vote_num

 
