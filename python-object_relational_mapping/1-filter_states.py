import MySQLdb
import sys
if __name__ == "__main__":
    # Vérifie si le bon nombre d'arguments est passé
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)
    
    # Récupère les arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Connexion à la base de données MySQL
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
    
    # Créer un curseur pour exécuter la requête SQL
    cursor = db.cursor()
    
    # Requête SQL pour filtrer les états dont le nom commence par 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    
    # Exécute la requête
    cursor.execute(query)
    
    # Récupère les résultats
    states = cursor.fetchall()
    
    # Affiche les résultats
    for state in states:
        print(state)
    
    # Ferme la connexion
    cursor.close()
    db.close()

