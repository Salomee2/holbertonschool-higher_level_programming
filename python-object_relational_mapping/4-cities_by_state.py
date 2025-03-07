#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
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
	
	# Création d'un curseur pour exécuter les requêtes
	cursor = db.cursor()
	
	# Requête SQL pour récupérer toutes les villes avec leur état
	query = """
	SELECT cities.id, cities.name, states.name 
	FROM cities 
	JOIN states ON cities.state_id = states.id 
	ORDER BY cities.id;
	"""
	cursor.execute(query)
	
	# Récupération et affichage des résultats
	for row in cursor.fetchall():
		print(row)
	
	# Fermeture du curseur et de la connexion
	cursor.close()
	db.close()
