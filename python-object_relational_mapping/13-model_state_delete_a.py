#!/usr/bin/python3
"""script that deletes all State objects with
a name containing the letter a
from the database hbtn_0e_6_usa
"""

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
        session.query(State)\
            .filter(State.name.like(f"%a%")).delete()
        session.commit()


if __name__ == "__main__":
    main()
