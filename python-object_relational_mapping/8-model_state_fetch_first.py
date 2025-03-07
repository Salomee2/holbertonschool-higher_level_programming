#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def fetch_first_state():
    # Récupérer les arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Créer l'URL de connexion à MySQL avec SQLAlchemy
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Créer la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer le premier état dans la table
    state = session.query(State).first()

    # Vérifier si la table est vide
    if state is None:
        print("Nothing")
    else:
        print(state)

    # Fermer la session
    session.close()

if __name__ == "__main__":
    fetch_first_state()
