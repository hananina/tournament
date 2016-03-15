#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""

    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    conn = connect()
    c = conn.cursor()
    c.execute("TRUNCATE matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""

    conn = connect()
    c = conn.cursor()
    c.execute("TRUNCATE players;")
    conn.commit()
    c.execute("TRUNCATE playerstandings;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""

    conn = connect()
    c = conn.cursor()
    c.execute("SELECT id_player, COUNT (id_player) as num FROM players GROUP BY id_player;")
    result = c.rowcount
    conn.close()
    return result


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO Players(name) values(%s);", (name,))
    conn.commit()
    conn.close()


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

    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO playerstandings(id_player, name) (SELECT id_player, name FROM players\
                GROUP BY id_player,name);")
    conn.commit()    
    c.execute("UPDATE playerstandings SET wins = (SELECT COUNT (id_winner) FROM matches\
                where matches.id_winner = playerstandings.id_player);")
    conn.commit()
    c.execute("UPDATE playerstandings SET matches = (SELECT COUNT(*) FROM matches \
                WHERE playerstandings.id_player = matches.id_winner \
                or playerstandings.id_player = matches.id_loser);")
    conn.commit()
    c.execute("select * from playerstandings ORDER BY wins desc;")
    conn.commit()
    standings = c.fetchall()
    conn.close()
    return standings


def reportMatch(winner,loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO matches(id_winner,id_loser) values(%s,%s);", (winner,loser))
    conn.commit()
    c.execute("UPDATE playerstandings SET wins = (SELECT COUNT (id_winner) FROM matches \
                where matches.id_winner = playerstandings.id_player);")
    conn.commit()
    c.execute("UPDATE playerstandings SET matches = (SELECT COUNT(*) FROM matches \
                WHERE playerstandings.id_player = matches.id_winner \
                or playerstandings.id_player = matches.id_loser);")
    conn.commit()
    conn.close()


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

    conn = connect()
    c = conn.cursor()
    c.execute("SELECT id_player, name FROM playerstandings ORDER BY wins DESC;")
    conn.commit()
    results = c.fetchall()
    conn.close()
    #make an array to store tupples.
    final_pairing = []
    #how many records you have in results.
    thislen = len(results) 
    for i in range(0, thislen, thislen * 1/2):
        id1   = results[i][0]
        name1 = results[i][1]
        id2   = results[i+1][0]
        name2 = results[i+1][1]
        pairing = (id1, name1, id2, name2)
        final_pairing.append(pairing)
    return final_pairing