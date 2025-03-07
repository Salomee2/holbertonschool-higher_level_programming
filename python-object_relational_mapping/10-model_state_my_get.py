#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    # Vérification que le nombre d'arguments est correct
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Récupération des arguments
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Création de l'URL de connexion
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost/{db_name}')
    
    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de l'état dans la base de données
    state = session.query(State).filter(State.name == state_name).first()

    # Affichage du résultat
    if state:
        print(state.id)
    else:
        print("Not found")
