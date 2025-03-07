#!/usr/bin/python3
"""
Define the City class that links to the MySQL table `cities`
inherits from Base
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class that links to the `cities` table in the database
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id
