-- Table definitions for the tournament project.
--


-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--



CREATE TABLE players (id_player serial, name varchar(80));
--win_recordいらん！！！！

-- players
  -- serial ID
  -- name

  -- ALTER TABLE players ADD win_record int;


-- CREATE TABLE tournament (size int, size_players int, size_rounds int, size_mutches int);

-- size of tournament
  -- total number of the players 
  -- how many rounds? =  log2 n (3) 
  -- how many matches? = n -- 1 (7)



--playerstandings
CREATE TABLE playerstandings(id_player int, name varchar(80), wins int, matches int);




CREATE TABLE matches(id_match serial, id_winner int, id_loser int);
--これはidをid_playerと共有している。
-- matches
  -- match number: match 1
  -- winner: 
  -- loser:



-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


