#!/usr/bin/python3
"""script that changes the name of a State object
from the database hbtn_0e_6_usa
Change the name of the State where id = 2 to New Mexico"""

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
        state_to_update = session.query(State)\
            .filter(State.id == 2).all()
        if state_to_update:
            state_to_update[0].name = "New Mexico"
            session.commit()
        else:
            print("Not found")


if __name__ == "__main__":
    main()
