#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa.
Prevents SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données MySQL
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)
    cur = conn.cursor()

    # Requête sécurisée (préparée) pour éviter les injections SQL
    query = """
        SELECT cities.id, cities.name, states.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Récupération des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture de la connexion
    cur.close()
    conn.close()
