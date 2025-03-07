import MySQLdb

# Connexion à la base de données MySQL
conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()

# Exécution d'une requête simple
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()

# Affichage des résultats
for row in rows:
    print(row)

# Fermeture de la connexion
cur.close()
conn.close()
