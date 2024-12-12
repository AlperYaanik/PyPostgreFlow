import json
import psycopg

#Load configuration files containing credential keys for the database
def load_config():
    try:
        with open("config.json", "r") as file:
            config= json.load(file)
        return config
    except FileNotFoundError:
        print("Error: The file at config.json was not found")
        return None
    except json.JSONDecodeError:
        print("Error: config.json could not decoded")
        return None            


#Connect to PostgreSQL database
def postgres_connect():
    config =load_config()
    if config:
        db_name = config["postgres_db"]["database"]
        db_pass = config["postgres_db"]["password"]
        db_user = config["postgres_db"]["user"]
        db_port = config["postgres_db"]["port"]
        db_host = config["postgres_db"]["host"]
        db_table = config["postgres_db"]["table"]
    try:  
        conn =  psycopg.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host, port = db_port )
        return conn,db_table
    except psycopg.Error as e :
        print(f' PostgreSQL Error: {e}')
        return None,None


#Insert data into a table in the PostgreSQL database
def insert_data_into_postgres(data):
    """config =load_config()
    if config:
        db_table = config["postgres_db"]["table"]
"""
    connection,db_table = postgres_connect()
    """  if connection is None:
            print("Database connection is failed")
            return None"""

    cursor = connection.cursor()
    query= """
    INSERT INTO {} (ip, datetime, http_method, resource, protocol_version, status, response_time, referrer, user_agent, process_time)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """.format(db_table)
    try:
        data_values = [(row['ip'],row['datetime'],row['http_method'],row['resource'],row['protocol_version'],\
                            row['status'],row['response_time'],row['referrer'],row['user_agent'],row['process_time']) for row in data]
   
        cursor.executemany(query,data_values)
        connection.commit()
        print("Insert transaction is done")
    except psycopg.Error as e :  
        print(f'PostgreSQL Error: {e}')
    finally:   
        
        cursor.close()
        connection.close() 
        return
    

     