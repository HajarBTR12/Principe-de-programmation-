import mysql.connector #pip3.instale mysql-connector-python
from mysql.connector import Error
from config import DB_CONFIG
def get_conection ():
    #Crée et retourne une nouvelle conxion MYSQL.
    #lève une exception si la connexon échoue.
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Erreur connexion MySQL : {e}")
        raise
 #**BD_config : decomposer lobjet cle val
