#!/usr/bin/python3
"""Safe script to filter states by user input, preventing SQL injections"""
import MySQLdb
import sys

if __name__ == "__main__":
	# Connexion à la base de données MySQL
	db = MySQLdb.connect(
		host="localhost",
		user=sys.argv[1],
		passwd=sys.argv[2],
		db=sys.argv[3],
		port=3306
	)
	cursor = db.cursor()

	# Requête sécurisée avec des paramètres
	query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
	cursor.execute(query, (sys.argv[4],))

	# Affichage des résultats
	rows = cursor.fetchall()
	for row in rows:
		print(row)

	# Fermeture de la connexion
	cursor.close()
	db.close()
