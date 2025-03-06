#!/usr/bin/python3
"""module creating state model"""

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Column, Integer
import sys

"""creation of base class, that will be used to define table"""
Base = declarative_base()


class State(Base):
    """defining the class State / MySQL table states
    with 2 class attributes
    corresponding to 2 colums
    """
    __tablename__ = "states"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
        )
    name = Column(
        String(128),
        nullable=False
        )


if __name__ == "__main__":
    """connection to db"""
    username = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    query = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, pw, db)
    engine = sa.create_engine(query)

    """cretaed tables in db (if non existing)"""
    Base.metadata.create_all(engine)
