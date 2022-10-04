import flask
from flask import request, jsonify, render_template
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Get Products
@app.route('/api/customer/GetCustomers', methods=['GET'])
def GetCustomers():
    customerList = []
    try:
        db=sqlite3.connect('Inventory.db')
        db.row_factory = sqlite3.Row
        cur = db.cursor()
        cur.execute("SELECT * FROM CustomerTbl")
        rows = cur.fetchall()

        for i in rows:
            customer = {}
            customer["CustomerId"] = i["CustomerId"]
            customer["CustomerName"] = i["CustomerName"]
            customer["CustomAddress"] = i["CustomAddress"]
            customer["CustomerMobil"] = i["CustomerMobil"]
            
            customerList.append(customer)

    except:
        customerList = []

    return customerList
 
 #Add Customer
@app.route('/api/customer/AddCustomer', methods=['POST'])
def AddCustomer():
    customer = request.get_json() 
    customerList = {}
    db=sqlite3.connect('Inventory.db')
    try:        
        cur =db.cursor()
        cur.execute("INSERT INTO CustomerTbl (CustomerId, CustomerName, CustomAddress, CustomerMobil) VALUES (?, ?, ?, ?)", (customer['CustomerId'], customer['CustomerName'], customer['CustomAddress'], customer['CustomerMobil']))
        db.commit()
        customerList = GetCustomers()
    except:
        db.rollback()

    finally:
        db.close()

    return customerList

#Update Customer
@app.route('/api/customer/UpdateCustomer', methods=['POST'])
def UpdateCustomer():
    customer = request.get_json()
    customerList = {}
    db=sqlite3.connect('Inventory.db')
    try:        
        cur =db.cursor()
        cur.execute("UPDATE CustomerTbl SET CustomerName = ?, CustomAddress = ?, CustomerMobil = ? WHERE CustomerId =?",  
                     (customer['CustomerName'], customer['CustomAddress'], customer['CustomerMobil'], customer['CustomerId']))
        db.commit()
        customerList = GetCustomers()
    except:
        db.rollback()

    finally:
        db.close()

    return customerList
    
#Delete Customer
@app.route('/api/customer/DeleteCustomer/<int:cuustomerid>', methods=['DELETE'])
def DeleteCustomer(cuustomerid):
    message = {}
    db=sqlite3.connect('Inventory.db')
    try:        
        cur =db.cursor()
        cur.execute("DELETE from CustomerTbl WHERE CustomerId = ?",     
                      (cuustomerid,))
        db.commit()
        message["status"] = "Deleted"
    except:
        db.rollback()
        message["status"] = "Error"
    finally:
        db.close()

    return message
    
app.run()