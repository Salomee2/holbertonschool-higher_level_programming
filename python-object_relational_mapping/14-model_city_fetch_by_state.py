#!/usr/bin/python3
"""
Fetch all City objects from the database hbtn_0e_14_usa
and display them with their state
"""

from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    # Connexion à la base de données
    engine = create_engine('mysql://root:root@localhost/hbtn_0e_14_usa')
    Base.metadata.create_all(engine)  # Crée les tables si elles n'existent pas

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Définir les relations après avoir importé les classes
    State.cities = relationship("City", back_populates="state")
    City.state = relationship("State", back_populates="cities")

    # Exemple de requête
    cities = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()
    for city, state in cities:
        print(f"{city.id}: {city.name} -> {state.name}")

if __name__ == "__main__":
    main()
