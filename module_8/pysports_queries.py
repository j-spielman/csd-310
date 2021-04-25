# Joey Spielman| Module 8.3| Queries
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
#test that connection is made
try:
    """ try/catch block for handling potential MySQL database errors """ 
    db = mysql.connector.connect(**config) 
    #open cursor
    cursor = db.cursor()
    # Query the Team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # Get all results 
    teams = cursor.fetchall()
    #Output Team query
    print("\n  -- DISPLAYING TEAM RECORDS --")
    #loop through each team and format display
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # Query the Player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # Get all results
    players = cursor.fetchall()
    #Output Player query
    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    #Loop through each player and format display
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")
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