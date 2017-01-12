-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Deletes the database if it exists to avoid any errors
DROP DATABASE IF EXISTS tournament;

-- Create the database tournament
CREATE DATABASE tournament;

-- Connect to the database 
\c tournament;

-- Creates the players table which include the name and player_id
-- of the players. player_id will be generated by the database

CREATE TABLE players (
        player_id serial PRIMARY KEY,
        player_name varchar (50) NOT NULL
);


-- Creates results table to hold the match id's and player_id's
-- that correspond with the winner and loser of the match

CREATE TABLE results (
        match_id serial PRIMARY KEY,
        match_winner integer REFERENCES players(player_id) ON DELETE CASCADE,
        match_loser integer REFERENCES players(player_id) ON DELETE CASCADE
);

-- Creates a view standings table, that will be sorted by total_wins
-- and then by total_matches

CREATE VIEW standings AS
SELECT players.player_id, players.player_name,
(SELECT count(results.match_winner)
    FROM results
    WHERE players.player_id = results.match_winner)
    AS total_wins,
(SELECT count(results.match_id)
    FROM results
    WHERE players.player_id = results.match_winner
    OR players.player_id = results.match_loser)
    AS total_matches
FROM players
ORDER BY total_wins DESC, total_matches DESC;