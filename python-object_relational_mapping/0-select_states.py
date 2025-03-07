#!/usr/bin/python3
import MySQLdb
import sys

def list_databases():
    """Liste toutes les bases de données d'un serveur MySQL"""
    # Récupérer les arguments passés en ligne de commande
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion au serveur MySQL
    connection = MySQLdb.connect(host="localhost", user=user, passwd=password, db=db_name)

    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")

    # Récupérer toutes les bases de données
    databases = cursor.fetchall()

    # Afficher les bases de données
    for database in databases:
        print(database)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    list_databases()

