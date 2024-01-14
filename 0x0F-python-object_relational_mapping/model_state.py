#!/usr/bin/python3
"""
This defines a State class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This class has
    -id (integer, auto-generated, unique, not nullable, primary key)
    - name (string, up to 128 characters, not nullable)
    """
    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
