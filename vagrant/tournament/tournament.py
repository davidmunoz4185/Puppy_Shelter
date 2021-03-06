#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):

    """
    Creates database connection and cursor object, throws exception if
    there is a connection error
    """

    try:
        db_connect = psycopg2.connect("dbname={}".format(database_name))
        cursor = db_connect.cursor()
        return db_connect, cursor
    except psycopg2.Error:
        print "Cannot db_connect to database"


def deleteMatches():
    """
    Removes all results records such as wins, lossses and match
    id's from the database.
    'query' stores the postgresql commands to be executed by the
    cursor object which wipes the table.
    db_connect() commits changes and closes the database.
    """

    db_connect, cursor = connect()
    query = ("DELETE FROM results;")
    cursor.execute(query)
    db_connect.commit()
    db_connect.close()


def deletePlayers():
    """
    Removes all the player records from the database.
    'query' stores the posgresql commands to be executed by the
    cursor object which wipes the table.
    db_connect() commits changes and closes the database.
    """

    db_connect, cursor = connect()
    query = ("DELETE FROM players;")
    cursor.execute(query)
    db_connect.commit()
    db_connect.close()

def countPlayers():
    """Returns the number of players ready to play a match.
    'query' stores the postgresql commands to be executed by the
    cursor object which will return a count of all the players
    in the players table.
    'player_count' stores the list of  players tuples
    returned by database.
    db_connect() closes the database.
    """

    db_connect, cursor = connect()
    query = ("SELECT count(*) AS player_count FROM players;")
    cursor.execute(query)
    player_count = cursor.fetchone()[0]
    db_connect.close()
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db_connect, cursor = connect()
    query = ("INSERT INTO players(player_id, player_name) VALUES (default, %s);")
    cursor.execute(query, (name,))
    db_connect.commit()
    db_connect.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db_connect, cursor = connect()
    query = ("SELECT * FROM standings;")
    cursor.execute(query)
    matches = cursor.fetchall()
    db_connect.close()
    return matches

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    db_connect, cursor = connect()
    query = ("INSERT INTO results(match_id, match_winner, match_loser) VALUES (default, %s, %s);")
    cursor.execute(query, (winner, loser,))
    db_connect.commit()
    db_connect.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pair = []

    db_connect, cursor = connect()
    query = ("SELECT player_id, player_name FROM standings ORDER BY total_wins DESC;")
    cursor.execute(query)
    win_pair_list = cursor.fetchall()

    if len(win_pair_list) % 2 == 0:
        for i in range(0, len(win_pair_list), 2):
            collect_players = win_pair_list[i][0], win_pair_list[i][1], win_pair_list[i+1][0], win_pair_list[i+1][1]
            pair.append(collect_players)
        return pair

    else:
        print "There are an uneven number of players in the tournament"

    db_connect.close()

