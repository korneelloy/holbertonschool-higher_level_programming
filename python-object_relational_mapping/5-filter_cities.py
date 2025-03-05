#!/usr/bin/python3

"""script that lists all cities from the database hbtn_0e_4_usa"""


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

        query = "SELECT cities.name\
            FROM cities INNER JOIN states ON cities.state_id=states.id\
                WHERE states.name = %s ORDER BY cities.id"

        cursor.execute(query, (state_name,))

        allCities = cursor.fetchall()
        count = 0
        for city in allCities:
            if count != 0:
                print(", ", end="")
            print(city[0], end="")
            count += 1
        print('')

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    main()
