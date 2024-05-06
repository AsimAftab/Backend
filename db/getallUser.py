import sqlite3
import json

import sqlite3
import json

def getAllUser():
    conn = sqlite3.connect("medicalShop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MEDICINE")
    users = cursor.fetchall()
    conn.close()

    userJson = []
    for user in users:
        tempUser = {
            "user_id": user[1],
            "password": user[2],
            "Level": user[3],
            "DateofAccountCreation": user[4],
            "approved": user[5],
            "name": user[6],
            "Address": user[7],
            "email": user[8],
            "phone": user[9],
            "PinCode": user[10]
        }
        userJson.append(tempUser)
       
    return json.dumps(userJson)

def getSpecificUser(userId):
    conn = sqlite3.connect("medicalShop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MEDICINE WHERE user_id = ?", (userId,))
    users = cursor.fetchall()
    conn.close()

    userJson = []
    for user in users:
        tempUser = {
            "user_id": user[1],
            "password": user[2],
            "Level": user[3],
            "DateofAccountCreation": user[4],
            "approved": user[5],
            "name": user[6],
            "Address": user[7],
            "email": user[8],
            "phone": user[9],
            "PinCode": user[10]
        }
        userJson.append(tempUser)
    return json.dumps(userJson)
       
