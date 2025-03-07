#!/usr/bin/python3
"""
Script qui liste tous les états de la table 'states' d'une base MySQL.
"""

import sys
import MySQLdb

if __name__ == "__main__":
	# Recuperer les arguments passes au script
	# sys.argv[1] = username, sys.argv[2] = password, sys.argv[3] = database
	db = MySQLdb.connect(
		host="localhost",
		user=sys.argv[1],
		passwd=sys.argv[2],
		db=sys.argv[3],
		port=3306
	)

	# Creer un curseur pour executer des requetes SQL
	cursor = db.cursor()

	# Executer la requete pour recuperer tous les etats tries par id
	cursor.execute("SELECT * FROM states ORDER BY id ASC")

	# Recuperer et afficher les resultats
	for row in cursor.fetchall():
		print(row)

	# Fermer le curseur et la connexion
	cursor.close()
	db.close()
