#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>")
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

    # Recherche de l'état avec id=2 et mise à jour de son nom
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
