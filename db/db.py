import datetime
import sqlite3
import uuid
def create_table():
    conn = sqlite3.connect("medicalShop.db")
    cursor=conn.cursor()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS MEDICINE(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR(255), password VARCHAR(255), Level Integer, DateofAccountCreation DATE, approved BOOLEAN,name VARCHAR(255), Address VARCHAR(255), email VARCHAR(255), phone VARCHAR(255), PinCode VARCHAR(255));
    ''')

    conn.commit()
    conn.close()
    
def createUser(name,password,Address,Email,Phone,PinCode):
    conn=sqlite3.connect("medicalShop.db")
    cursor=conn.cursor()
    user_id=str(uuid.uuid4())
    dateofAccountCreation=datetime.datetime.today().strftime('%Y-%m-%d')
    cursor.execute("""INSERT INTO MEDICINE
               (user_id,password,Level,DateofAccountCreation,approved,name,Address,email,phone,PinCode)
               VALUES(?,?,?,?,?,?,?,?,?,?)""",
               (user_id, password, -1, dateofAccountCreation, 0, name, Address, Email, Phone, PinCode))

    conn.commit()
    conn.close() 
    return True

def GetAllUser():
    pass