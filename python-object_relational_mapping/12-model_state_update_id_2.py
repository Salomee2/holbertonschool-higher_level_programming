#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def update_state():
    """
    Changes the name of the State where id = 2 to 'New Mexico' in the database.
    """
    # Connection arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine that connects to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find the state with id = 2 and change its name
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = 'New Mexico'
        session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    update_state()
