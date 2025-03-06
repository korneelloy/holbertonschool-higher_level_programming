#!/usr/bin/python3
"""script that lists all City objects
from the database hbtn_0e_14_usa"""

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City


def main():
    """connection to db"""
    username = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    query = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, pw, db)
    engine = sa.create_engine(query)

    """creation of session"""
    Session = sessionmaker(bind=engine)

    """using built in method of sessions"""
    with Session() as session:
        cities = session.query(State.name, City.id, City.name)\
            .join(City, State.id == City.state_id)\
            .order_by(City.id).all()
        for city in cities:
            print(f"{city[0]}: ({city[1]}) {city[2]}")


if __name__ == "__main__":
    main()
