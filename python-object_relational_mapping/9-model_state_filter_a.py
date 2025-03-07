#!/usr/bin/python3
"""
Script that lists all State objects containing the letter 'a' from the database
hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def filter_states_by_letter_a():
    """
    List all State objects from the database hbtn_0e_6_usa that
    contain the letter 'a'
    """
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

    # Fetch all states that contain 'a' in the name, ordered by id
    states = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    filter_states_by_letter_a()
