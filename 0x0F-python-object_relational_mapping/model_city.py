#!/usr/bin/python3
"""Define mapper configuration for cities table"""


import MySQLdb
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """The class City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
