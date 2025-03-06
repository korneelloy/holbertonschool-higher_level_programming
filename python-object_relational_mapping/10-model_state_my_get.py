#!/usr/bin/python3
"""script that lists 1st State objects
from the database hbtn_0e_6_usa"""

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


def main():
    """connection to db"""
    username = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    query = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, pw, db)
    engine = sa.create_engine(query)

    """creation of session"""
    Session = sessionmaker(bind=engine)

    """using built in method of sessions"""
    with Session() as session:
        state = session.query(State)\
            .filter(State.name == state_name).all()
        if not state:
            print("Not found")
        else:
            print(f"{state[0].id}")


if __name__ == "__main__":
    main()
