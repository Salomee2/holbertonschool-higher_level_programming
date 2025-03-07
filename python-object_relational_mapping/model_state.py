#!/usr/bin/python3
"""Define a State class and Base for SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a Base instance for SQLAlchemy
Base = declarative_base()

class State(Base):
    """State class that links to the `states` table in MySQL"""

    # Define the table name in MySQL
    __tablename__ = 'states'

    # Define the columns and their properties
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
