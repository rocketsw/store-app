import mysql.connector
import json

first_name_pos=0
last_name_pos=1
street_pos=2
city_pos=3
state_pos=4
zipcode_pos=5
phone_pos=6

jsonInsertStr1 = '{"last":"Wayne","first":"John","street":"555 East St","city":"Anytown","state":"CA","zipcode":"30000","phone":"555-200-1234"}'
jsonInsertStr2 = '{"last":"Barker","first":"Bob","street":"234 West St","city":"Hometown","state":"TX","zipcode":"40000","phone":"999-300-4567"}'

class CustomerDB:

    def __init__(self):
	   # connect to database at startup (connections take time so only connect once)
       print("CustomerDB constructor")
       print("connecting to database")
       self.db = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='devl')

    def __del__(self):
       print("CustomerDB destructor")
       self.db.close()

    def getCustomerByID(self, id):
        print('id = ' + str(id))
        cursor = self.db.cursor()
        cursor.execute("select lastname, firstname from customer where customerid = %s" % (id) )
        results = cursor.fetchone()
        customerjson = '{"lastname":"' + results[last_name_pos] + '","firstname":"' + results[first_name_pos] + '"}'
        return customerjson

    def getCustomers(self):
        cursor = self.db.cursor()
        cursor.execute("select firstname, lastname, street, city, state, zipcode, phone from customer")
        customerjson = '['
        for (firstname, lastname, street, city, state, zipcode, phone) in cursor:
            if len(customerjson) > 1:
                customerjson = customerjson + ','
            customerjson = customerjson + '{"firstname":"' + firstname + '","lastname":"' + lastname  + '","street":"' + street + '","city":"' + city + '","state":"' + state + '","phone":"' + phone + '"}'
        customerjson = customerjson + ']'
        print('customerjson: ' + customerjson )
        return customerjson

    def getCustomersNext(self, numRows):
        return ""

    def insertCustomer(self, jsonstr):
        maxIdSQL = 'select max(CustomerID) from Customer;'
        cursor = self.db.cursor()
        cursor.execute(maxIdSQL)
        results = cursor.fetchone()
        maxId = results[0]
        print("max id: " + str(maxId))
        newId = maxId+1

        print(jsonstr)
        cdict = json.loads(jsonstr)
        print("customer firstname: " + cdict["first"])
        #insert into CUSTOMER values (0, 'John', 'Jones', '100 Main St','Anytown', 'VA', '10000', '555-100-1000');
        insertSqlStr = 'insert into CUSTOMER values (' + str(newId) + ',\''  + cdict['last'] + '\',\'' + cdict['first'] + '\',\'' + cdict['street'] + '\',\'' + cdict['city'] + '\',\'' + cdict['state'] + '\',\'' + cdict['zipcode'] + '\',\'' + cdict['phone'] + '\')'
        print(insertSqlStr)
        cursor.execute(insertSqlStr)
        self.db.commit()
        return newId

#Before executing a script, the Python interpreter will define a few special variables.
#For example, if the python interpreter is running the source file as the main program,
#  it sets the special __name__ variable to have a value "__main__".
#If this file is being imported from another module,
#  __name__ will be set to the module's name.
if __name__ == "__main__":
   cust = CustomerDB()
   #jsonstr = cust.getCustomerFromDB(1)
   #jsonstr = cust.getCustomersAndCountry()
   #jsonstr = cust.getCustomerByID(0)
   #newId = cust.insertCustomer(jsonInsertStr2)
   #print("new max ID = " + str(newId))
   #jsonstr = cust.getCustomerByID(newId)

   custJsonStr = cust.getCustomers()

   #print('customer json = {}'.format(jsonstr))
