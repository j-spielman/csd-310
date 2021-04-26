#Joey Spielman Module 9
#Query player and team table with a join query
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 
    db = mysql.connector.connect(**config) 
    #open cursor
    cursor = db.cursor()
    # Query the player table joined to the team table on team_id
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player LEFT OUTER JOIN team ON player.team_id = team.team_id")

    # Get all results 
    players = cursor.fetchall()
    #Output Team query
    print("\n  -- DISPLAYING PLAYER RECORDS --")
    #loop through each player and format display
    for player in players: 
        print("  Team ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

  
#Handle errors
except mysql.connector.Error as err:
    """ handle errors """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    #close connection
    db.close()