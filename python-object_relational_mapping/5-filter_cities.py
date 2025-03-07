#!/usr/bin/python3
"""
Script qui affiche toutes les villes d'un état donné
depuis la base de données hbtn_0e_4_usa.
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

	# Requête SQL sécurisée pour éviter les injections SQL
	query = """
		SELECT cities.name FROM cities
		JOIN states ON cities.state_id = states.id
		WHERE states.name = %s
		ORDER BY cities.id ASC
	"""

	# Exécuter la requête avec un paramètre sécurisé
	cursor.execute(query, (sys.argv[4],))

	# Récupérer les résultats
	cities = [row[0] for row in cursor.fetchall()]

	# Afficher les villes sous forme de liste séparée par des virgules
	print(", ".join(cities))

	# Fermer le curseur et la connexion
	cursor.close()
	db.close()
