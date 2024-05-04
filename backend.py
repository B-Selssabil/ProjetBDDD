import pymongo
import datetime
import mysql.connector
import hashlib

host = '127.0.0.1'
user = 'root'
password = 'helloworld19'
database = 'ProjetBDD'

# Part 1 : MongoDB

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ProjetBDD"]  
collection = db["Comment"]  
collection_users = db["Users"]  

def addComment(ID, comment):
    current_date_time = datetime.datetime.now()
    date_comment = current_date_time.strftime("%Y-%m-%d %H:%M")
    data = {"commentID": ID, "comment": comment, "date": date_comment}
    inserted_doc = collection.insert_one(data)
    print("ID du document inséré:", inserted_doc.inserted_id)
def getComments():
    comments = collection.find() 
    return comments
def updateComment(ID, comment):
    update_query = {"commentID": ID}
    new_values = {"$set": {"comment": comment}}
    collection.update_one(update_query, new_values)
    updated_doc = collection.find_one(update_query)
    print("Document mis à jour:", updated_doc)
def deleteComment(ID):
    delete_query = {"commentID": ID}
    result = collection.delete_one(delete_query)
    print("Deleted count:", result.deleted_count)


# Part 2 : MySQL

def connecting():
        
    connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )

    if connection.is_connected():
            print(f"Using database: {database}")
        
    return connection


def createDatabase():
    connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
            )
    cursor = connection.cursor()
    create_database_query = "CREATE DATABASE IF NOT EXISTS ProjetBDD"
    cursor.execute(create_database_query)

def createTableUsers():

    connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database = database
            )
    cursor = connection.cursor()   
    create_table_query = """
        CREATE TABLE IF NOT EXISTS Users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name varchar(10),
            email varchar(20),
            password varchar(300)

        )
        """
    cursor.execute(create_table_query)

def getUsers():
     
    connection = connecting()
    cursor = connection.cursor()
    query = "SELECT * FROM Users"
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def addUser(name, email, password):
     
    connection = connecting()
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO Users (name, email, password)
    VALUES (%(name)s, %(email)s, %(password)s)
    """

    encoded_password = hashlib.sha256(password.encode()).hexdigest()
    print(len(encoded_password))

    user_data = {
    'name': name,
    'email': email,
    'password': encoded_password

}
    cursor.execute(insert_query, user_data)
    connection.commit()

def updateUser(name, email, password):

    connection = connecting()
    cursor = connection.cursor()        
    if len(email) > 0  and len(password) == 0:
        update_query = """
        UPDATE Users
            SET email = %(email)s
            WHERE name = %(name)s;
        """
        user_data = {
        'name': name,
        'email': email
        }
    elif len(password) > 0 and len(email) == 0:
        encoded_password = hashlib.sha256(password.encode()).hexdigest()
        update_query = """
        UPDATE Users
            SET password = %(encoded_password)s
            WHERE name = %(name)s;
        """
        user_data = {
        'name': name,
        'encoded_password': encoded_password
        }

    else :
        encoded_password = hashlib.sha256(password.encode()).hexdigest()
        update_query = """
        UPDATE Users
            SET password = %(encoded_password)s, email = %(email)s
            WHERE name = %(name)s;
        """
        user_data = {
        'name': name,
         'email':email,
        'encoded_password': encoded_password
        }


    cursor.execute(update_query, user_data)
    connection.commit()

def deleteUser(name):

    connection = connecting()
    cursor = connection.cursor()   
    delete_query = """
        DELETE FROM Users
        WHERE name = %(name)s;
        """
    user_data  = {
        'name':name
    }
    cursor.execute(delete_query, user_data)
    connection.commit()

def createTable():
    connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS Comments (
            id INT PRIMARY KEY,
            comment varchar(100),
            date varchar(30)
        )
        """
    cursor.execute(create_table_query)


def migrateToMongo():
    comments = getComments()
    connection = connecting()
    cursor = connection.cursor()
    for c in comments:
        insert_query = """
        INSERT INTO Comments (id, comment, date)
        VALUES (%(id)s, %(comment)s, %(date)s)
        """
        comment_data = {
            "id" : c['commentID'],
            "date":c['date'],
            "comment":c['comment']

        }
        get_querry = """
        SELECT * FROM Comments where id = %(id)s
        """
        cursor.execute(get_querry, comment_data)
        res = cursor.fetchall()
        if not res : 
            cursor.execute(insert_query, comment_data)
    connection.commit()

def migrateToMySQL():
    users = getUsers()
    for u in users :
        query = {"User_ID":u[0]}
        res = collection_users.find_one(query)
        if not res :
            data = {"User_ID": u[0], "Name": u[1], "Email": u[2], "Password":u[3]}
            inserted_doc = collection_users.insert_one(data)
   

#createDatabase()
#createTableUsers()
# createTable()
# migrateToMongo()
# migrateToMySQL()
# addUser('Rania','ra_ttt@gmail.com','test')