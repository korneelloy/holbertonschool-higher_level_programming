#!/usr/bin/python3

"""script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys


def main():
    """main function to avoid execution when imported"""
    username = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    try:
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            password=pw,
            database=db
        )

        cursor = connection.cursor()

        query = "SELECT * FROM states WHERE `name` = '{}'\
           ORDER BY id".format(state_name)

        cursor.execute(query)

        statesWithStateName = cursor.fetchall()
        for states in statesWithStateName:
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
