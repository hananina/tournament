-- Table definitions for the tournament project.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;


CREATE TABLE players(
id_player serial PRIMARY KEY,
name varchar(80));


CREATE TABLE playerstandings(
id_player int,
name varchar(80),
wins int,
matches int);


CREATE TABLE matches(
id_match serial PRIMARY KEY,
id_winner int,
id_loser int);

