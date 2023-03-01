import configparser

import mysql.connector

def getConfig():
    config = configparser.ConfigParser()
    config.read_file(open(r'db.conf'))
    return config

# This function will return a connect object
def connect(config):

    # Establish a connection using the driver
    connection = mysql.connector.connect(
        host = config.get('database_credentials', 'host'),
        user = config.get('database_credentials','user'),
        password = config.get('database_credentials', 'password'),
        database = config.get('database_credentials', 'database'))
    #return 
    return connection

def disconnect(conn):
    conn.close()
    return None