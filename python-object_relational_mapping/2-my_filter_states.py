#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
	# Connexion à la base de données
	db = MySQLdb.connect(
		host="localhost",
		user=sys.argv[1],
		passwd=sys.argv[2],
		db=sys.argv[3],
		port=3306
	)

	# Création du curseur pour exécuter des requêtes
	cursor = db.cursor()

	# Exécution de la requête SQL avec format (ATTENTION: risque d'injection SQL)
	query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4])
	cursor.execute(query)

	# Récupération et affichage des résultats
	rows = cursor.fetchall()
	for row in rows:
		print(row)

	# Fermeture du curseur et de la connexion
	cursor.close()
	db.close()
