from flask import Flask, render_template, request, jsonify
from db.db import create_table, createUser
from db.getallUser import getAllUser, getSpecificUser



app = Flask(__name__)

@app.route('/CreateUser', methods=['POST'])
def create_user():
    Name = request.form['name']
    password = request.form['password']
    address = request.form['address']
    email = request.form['email']
    phone = request.form['phone']
    pinCode = request.form['pincode']
    dbRes = createUser(name=Name, password=password, Address=address, Email=email, Phone=phone, PinCode=pinCode)
    if dbRes == True:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"})

@app.route('/getAllUser', methods=['GET'])
def getAllUsers():

    return getAllUser()
@app.route('/getSpecificUser', methods=['GET'])
def getspecificuser():
    userId = request.args['userId']
  
    return getSpecificUser(userId=str(userId))
if __name__ == "__main__": 
    create_table()
    app.run(debug=True)