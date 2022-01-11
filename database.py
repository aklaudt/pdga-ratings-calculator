import sqlite3
from sqlite3 import Error
from player import Player


class Database:
    @staticmethod
    def createConnection(db_file_name):
        conn = None
        try:
            conn = sqlite3.connect(db_file_name)
            return conn
        except Error as e:
            print(e)

        return conn

    @staticmethod
    def run_sql(conn, sql_command):
        try:
            c = conn.cursor()
            c.execute(sql_command)
        except Error as e:
            print(e)
        pass

    @staticmethod
    def createPlayersTable(conn):
        sql_create_playes_table = """   CREATE TABLE players (
                                        pdgaNumber integer PRIMARY KEY,
                                        name text NOT NULL,
                                        yearStarted integer NOT NULL,
                                        membershipExpired datetime NULL,
                                        status integer NOT NULL,
                                        classification text NULL,
                                        officialStatus text NULL, 
                                        officialStatusExpiration datetime NULL,
                                        currentRating integer NULL,
                                        careerEvents integer NULL,
                                        careerEarnings integer NULL,
                                        location text NULL
                                        );"""

        Database.run_sql(conn, sql_create_playes_table)

    @staticmethod
    def dropPlayersTable(conn):
        sql_drop_players_table = """ drop table if exists players"""
        Database.run_sql(conn, sql_drop_players_table)

    @staticmethod
    def addPlayerToDb(conn, player):
        try:
            c = conn.cursor()
            data_tuple = player.pdgaNumber, player.name, player.yearStarted, player.membershipExpired, player.status, player.classification, player.officialStatus, player.officialStatusExpiration, player.currentRating, player.careerEvents, player.careerEarnings, player.location
            c.execute(
                "INSERT INTO players(pdgaNumber, name, yearStarted, membershipExpired, status, classification, officialStatus, officialStatusExpiration, currentRating, careerEvents, careerEarnings, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data_tuple)
            conn.commit()
        except Error as e:
            print(e)

    @staticmethod
    def getHighestPdgaNumberInDb(conn):
        try:
            c = conn.cursor()
            c.execute(
                "SELECT pdgaNumber from players order by pdgaNumber desc LIMIT 1")
            number = c.fetchall()[0][0]
            return int(number)
        except Error as e:
            print(e)
