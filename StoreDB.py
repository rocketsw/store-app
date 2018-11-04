import mysql.connector
import json

first_name_pos=0
last_name_pos=1
street_pos=2
city_pos=3
state_pos=4
zipcode_pos=5
phone_pos=6

jsonInsertStr1 = '{"last":"Wayne","first":"John","street":"555 East St","city":"Anytown","state":"CA","zip":"30000","phone":"555-200-1234"}'
jsonInsertStr2 = '{"last":"Barker","first":"Bob","street":"234 West St","city":"Hometown","state":"TX","zip":"40000","phone":"999-300-4567"}'

class StoreDB:

    def __init__(self):
	   # connect to database at startup (connections take time so only connect once)
       print("StoreDB constructor")
       print("connecting to database")
       self.db = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='devl')

    def __del__(self):
       print("StoreDB destructor")
       self.db.close()

    def getCustomerByID(self, id):
        print('id = ' + str(id))
        customerjson = '{"lastname":"Smith","firstname":"John"}'
        return customerjson

    def getCustomers(self):
        print("inside StoreDB.getCustomers()")
        customerjson = '[{"id":"","first":"John","last":"Smith"}]'
        return customerjson

    def getCustomersNext(self, numRows):
        return ""

    def insertCustomer(self, jsonstr):
        newId = 1001
        return newId

#Before executing a script, the Python interpreter will define a few special variables.
#For example, if the python interpreter is running the source file as the main program,
#  it sets the special __name__ variable to have a value "__main__".
#If this file is being imported from another module,
#  __name__ will be set to the module's name.
if __name__ == "__main__":
   cust = StoreDB()
   #newId = cust.insertCustomer(jsonInsertStr2)
   #print("new max ID = " + str(newId))
   #jsonstr = cust.getCustomerByID(newId)
   custJsonStr = cust.getCustomers()
   print( custJsonStr )
