# Voter Information System
This database features sample voter and candidate data and the organization of this data into tables to create a model electio with ballots. This datebase has multiple tables to organize the data which include: voters, candidates, election, result.

## Requirements
To set up this database a user will need:
- macOS
- postgreSQL 15
- pgAdmin 4 GUI tool

## Tables
Key:
- **bold**: primary key
- *italics*: foreign key

### Candidate
- ***candidate_id***
- candidate_firstname
- candidate_middleinital
- candidate_lastname
- candidate_yearofbirth
- candidate_party
- *district_id*

### Voter
- ***voter_id***
- voter_firstname
- voter_middleinitial
- voter_lastname
- voter_yearofbirth
- voter_address
- *district_id*

### District
- ***district_id***
- district_name

### Ballot
- **ballot_id**
- *voter_id*
- *candidate_id*
- date_of_vote

### ElectionOutcome
- **electionoutcome_id**
- *candidate_id*
- did_win
- *district_id*
- vote_percentage
- election_year

