#!/usr/bin/python3

""" script that lists all states starting with N
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def main():
    """main function to avoid execution when imported"""
    username = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]

    try:
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            password=pw,
            database=db
        )

        cursor = connection.cursor()

        cursor.execute(
            '''SELECT * FROM states WHERE `name` LIKE 'N%' ORDER BY id '''
            )

        allStatesWithN = cursor.fetchall()
        for states in allStatesWithN:
            print(states)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    main()
