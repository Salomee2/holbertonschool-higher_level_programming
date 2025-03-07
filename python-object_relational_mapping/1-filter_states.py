#!/usr/bin/python3
"""
Script qui liste tous les états dont le nom commence par "N"
depuis la base de données hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
	# Connexion à la base de données
	db = MySQLdb.connect(
		host="localhost",
		user=sys.argv[1],
		passwd=sys.argv[2],
		db=sys.argv[3],
		port=3306
	)

	# Création du curseur pour exécuter la requête
	cursor = db.cursor()

	# Requête SQL : récupérer les états commençant par "N"
	cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

	# Récupérer et afficher les résultats
	for row in cursor.fetchall():
		print(row)

	# Fermer le curseur et la connexion
	cursor.close()
	db.close()
