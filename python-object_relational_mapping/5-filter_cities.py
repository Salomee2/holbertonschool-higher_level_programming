#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
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
	
	# Requête SQL sécurisée (SQL injection free)
	query = """
	SELECT cities.name FROM cities 
	JOIN states ON cities.state_id = states.id 
	WHERE states.name = %s 
	ORDER BY cities.id;
	"""
	cursor.execute(query, (sys.argv[4],))  # Utilisation de %s pour éviter l'injection SQL
	
	# Récupération et affichage des résultats sous forme de liste
	cities = [row[0] for row in cursor.fetchall()]
	print(", ".join(cities))
	
	# Fermeture du curseur et de la connexion
	cursor.close()
	db.close()
