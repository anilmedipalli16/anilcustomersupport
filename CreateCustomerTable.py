import sqlite3
db=sqlite3.connect('Inventory.db')
try:        
    cur =db.cursor()
    cur.execute('''CREATE TABLE CustomerTbl (
    CustomerId INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerName TEXT (50) NOT NULL,
    CustomAddress TEXT (100) NOT NULL,
    CustomerMobil TEXT (50) NOT NULL);''')
    print ('Success')
except:
    print ('Error')
    db.rollback()
db.close()