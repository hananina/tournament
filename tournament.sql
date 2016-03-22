-- Table definitions for the tournament project.
DROP DATABASE IF EXISTS tournament
CREATE DATABASE tournament;
\c tournament;


CREATE TABLE players(
  id_player serial PRIMARY KEY,
  name VARCHAR(80) NOT NULL,
  wins INTEGER DEFAULT 0,
  matches INTEGER DEFAULT 0
);


CREATE TABLE matches(
  id_match serial PRIMARY KEY,
  id_winner INTEGER REFERENCES players(id_player) ON DELETE CASCADE,
  id_loser INTEGER REFERENCES players(id_player) ON DELETE CASCADE,
  CHECK(id_loser != id_winner)
);
# 4th constraint is a table constraint.