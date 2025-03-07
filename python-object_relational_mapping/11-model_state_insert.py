#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Récupération des arguments
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Création de l'URL de connexion
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost/{db_name}')

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Création d'un nouvel objet State
    new_state = State(name="Louisiana")

    # Ajout de l'objet à la session et commit
    session.add(new_state)
    session.commit()

    # Affichage de l'ID du nouvel état
    print(new_state.id)
