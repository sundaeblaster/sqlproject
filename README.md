# Voter Information System
This database features sample voter and candidate data and the organization of this data into tables to create a model election with ballots. This datebase has multiple tables to organize the data which include: voter, candidate, ballot, electionoutcome.

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

## Sample Queries

##### Finds the name of the oldest voter
SELECT voter_firstname, voter_yearofbirth
FROM voter
WHERE voter_yearofbirth = (SELECT max(voter_yearofbirth) FROM voter)


##### Finds names of candidates who were born before 1969 and are in district 1.
SELECT candidate_firstname, candidate_yearofbirth, district_id
FROM candidate
WHERE candidate_yearofbirth < 1969 and district_id = 1


##### Finds the voter IDs of those who did not vote on 11-03-18
SELECT voter_firstname, date_of_vote
FROM voter, ballot
WHERE voter.voter_id = ballot.voter_id and date_of_vote not in ('11-03-18')
ORDER BY date_of_vote


##### Finds the name of a voter's dist
SELECT voter_firstname, district_name
FROM voter, district
WHERE voter.district_id = district.district_id





