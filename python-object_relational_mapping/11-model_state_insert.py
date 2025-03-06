#!/usr/bin/python3
"""cript that adds the State object
“Louisiana” to the database hbtn_0e_6_usa"""

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

    """cretaion of new state object"""
    Louisiana = State(name="Louisiana")

    """creation of session"""
    Session = sessionmaker(bind=engine)

    """using built in method of sessions"""
    with Session() as session:
        session.add(Louisiana)
        session.commit()
        last_state = session.query(State).order_by(State.id.desc()).first()
        print(f"{last_state.id}")


if __name__ == "__main__":
    main()
