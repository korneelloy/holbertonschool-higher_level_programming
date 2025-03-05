#!/usr/bin/python3

"""script that lists all cities from the database hbtn_0e_4_usa"""


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

        cursor.execute('''SELECT cities.id, cities.name, states.name
                       FROM cities
                       INNER JOIN states
                       ON cities.state_id=states.id
                       ORDER BY cities.id ''')

        allCities = cursor.fetchall()
        for city in allCities:
            print(city)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    main()
