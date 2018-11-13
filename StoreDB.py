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
jsonInsertStr3 = '{"last":"Sundaar","first":"Ravi","street":"500 Ashburn Farms Rd","city":"Ashburn","state":"VA","zip":"11111","phone":"804-222-3333"}'

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
        cursor = self.db.cursor()
        cursor.execute("select lastname, firstname from customer where customerid = %s" % (id) )
        results = cursor.fetchone()
        customerjson = '{"last":"' + results[last_name_pos] + '","first":"' + results[first_name_pos] + '"}'
        return customerjson

    def getCustomers(self):
        print("inside StoreDB.getCustomers()")
        cursor = self.db.cursor()
        cursor.execute("select CustomerID, firstname, lastname, street, city, state, zipcode, phone from customer")
        customerjson = '['
        for (CustomerID, first, last, street, city, state, zip, phone) in cursor:
            if len(customerjson) > 1:
                customerjson = customerjson + ','
            customerjson = customerjson + '{"id":"' + str(CustomerID) + '","first":"' + first + '","last":"' + last  + '","street":"' + street + '","city":"' + city + '","state":"' + state + '","zip":"' + zip + '","phone":"' + phone + '"}'
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

        #print(jsonstr)
        cdict = json.loads(jsonstr)
        print("customer firstname: " + cdict["first"])
        #insert into CUSTOMER values (0, 'John', 'Jones', '100 Main St','Anytown', 'VA', '10000', '555-100-1000');
        insertSqlStr = 'insert into CUSTOMER values (' + str(newId) + ',\''  + cdict['first'] + '\',\'' + cdict['last'] + '\',\'' + cdict['street'] + '\',\'' + cdict['city'] + '\',\'' + cdict['state'] + '\',\'' + cdict['zip'] + '\',\'' + cdict['phone'] + '\');'
        print(insertSqlStr)
        cursor.execute(insertSqlStr)
        self.db.commit()
        return newId

    def updateCustomer(self, jsonstr):
        #print(jsonstr)
        cdict = json.loads(jsonstr)
        id = cdict['id']
        print("customer id: " + id)
        updateSqlStr = 'update CUSTOMER set FirstName = "' + cdict['first'] + '", LastName = "' + cdict['last'] + '", Street = "' + cdict['street'] + '", City = "' + cdict['city'] + '", State = "' + cdict['state'] + '", Zipcode = "' + cdict['zip'] + '", Phone = "' + cdict['phone'] + '" where CustomerID = ' + id;
        print(updateSqlStr)
        cursor = self.db.cursor()
        cursor.execute(updateSqlStr)
        self.db.commit()
        return id

#Before executing a script, the Python interpreter will define a few special variables.
#For example, if the python interpreter is running the source file as the main program,
#  it sets the special __name__ variable to have a value "__main__".
#If this file is being imported from another module,
#  __name__ will be set to the module's name.
if __name__ == "__main__":
   cust = StoreDB()
   #jsonstr = cust.getCustomerFromDB(1)
   #jsonstr = cust.getCustomersAndCountry()
   #jsonstr = cust.getCustomerByID(0)
   newId = cust.insertCustomer(jsonInsertStr3)
   #print("new max ID = " + str(newId))
   #jsonstr = cust.getCustomerByID(newId)

   #custJsonStr = cust.getCustomers()

   #print('customer json = {}'.format(jsonstr))
