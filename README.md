# Voter Information System
This database features sample voter and candidate data and the organization of this data into tables to create a model electio with ballots. This datebase has multiple tables to organize the data which include: voters, candidates, election, result.

## Requirements
To set up this database a user will need:
- macOS
- postgreSQL 15
- pgAdmin 4 GUI tool

## ERD Diagram
<img width="512" alt="Screenshot 2023-02-19 at 12 30 31 PM" src="https://user-images.githubusercontent.com/65120062/219964645-ec351c7c-6885-47eb-b623-6cab38aa7e61.png">

## Tables
#### Key:
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

[Candidate Sample Data](./candidate.csv)

### Voter
- ***voter_id***
- voter_firstname
- voter_middleinitial
- voter_lastname
- voter_yearofbirth
- voter_address
- *district_id*

[Voter Sample Data](./voter.csv)

### District
- ***district_id***
- district_name

[District Sample Data](./district.csv)

### Ballot
- **ballot_id**
- *voter_id*
- *candidate_id*
- date_of_vote

[Ballot Sample Data](./ballot.csv)

### ElectionOutcome
- **electionoutcome_id**
- *candidate_id*
- did_win
- *district_id*
- vote_percentage
- election_year

[ElectionOutcome Sample Data](./electionoutcome.csv)

## Queries

