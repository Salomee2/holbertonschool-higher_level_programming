#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

def filter_states():
    # Connexion à la base de données MySQL
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Créer l'URL de connexion pour MySQL
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)

    # Créer une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer les États contenant "a", triés par ID
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Affichage des résultats
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

if __name__ == "__main__":
    # Lancer la fonction si le script est exécuté directement
    filter_states()
