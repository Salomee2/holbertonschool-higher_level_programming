from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration de la connexion à MySQL via SQLAlchemy
engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_0_usa', pool_pre_ping=True)
Base = declarative_base()

# Définition de la classe State pour la table "states"
from sqlalchemy import Column, Integer, String

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

# Création de la session pour interagir avec la base de données
Session = sessionmaker(bind=engine)
session = Session()

# Demander à l'utilisateur d'entrer un nom d'état
state_name = input("Entrez le nom d'un état: ")

# Requête sécurisée avec filtre pour éviter les injections SQL
result = session.query(State).filter(State.name == state_name).all()

# Afficher les résultats
for state in result:
    print(f"{state.id}: {state.name}")

# Fermeture de la session
session.close()
