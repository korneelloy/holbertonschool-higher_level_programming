#!/usr/bin/python3
"""script that lists all State objects
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
    query = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, pw, db)
    engine = sa.create_engine(query)

    """creation of session"""
    Session = sessionmaker(bind=engine)

    """using built in method of sessions"""
    with Session() as session:
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
