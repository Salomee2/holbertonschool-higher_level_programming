#!/usr/bin/python3
"""
Define the State class and link to the MySQL table `states`
inherits from Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base


class State(Base):
    """
    State class that links to the `states` table in the database
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
