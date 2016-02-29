-- Table definitions for the tournament project.

CREATE DATABASE tournament;


CREATE TABLE players(
id_player serial,
name varchar(80));


CREATE TABLE playerstandings(
id_player int,
name varchar(80),
wins int,
matches int);


CREATE TABLE matches(
id_match serial,
id_winner int,
id_loser int);

