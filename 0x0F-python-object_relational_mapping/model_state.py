#!/usr/bin/python3
"""
This module contains the State Class that
will be the structure of the database.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """ State model class is a representation of a table,
    where each attribute is a column of it.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)
