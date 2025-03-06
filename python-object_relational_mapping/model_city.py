#!/usr/bin/python3
"""module creating city model"""

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Column, Integer, ForeignKey
import sys

"""creation of base class, that will be used to define table"""
Base = declarative_base()


class City(Base):
    """defining the class City / MySQL table cities
    with 2 class attributes
    corresponding to 3 colums
    """
    __tablename__ = "cities"

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
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
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
