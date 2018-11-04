from flask import Flask, render_template
from flask import request
from StoreDB import StoreDB

app = Flask(__name__)
#storedb = StoreDB()

@app.route('/')
def render():
   return render_template('index.html')

@app.route('/miapi.html')
def render_miapi():
   return render_template('miapi.html')

@app.route('/addCustomerToDB')
def addCustomerToDB():
    firstName = request.args.get('firstName', 'unknown')
    lastName = request.args.get('lastName', 'unknown')
    jsonstr = '{"first":"' + firstName + '","last":"' + lastName + '"}'
    print( jsonstr )
    #newId = storedb.insertCustomer( jsonstr )
    newId = 1000
    return firstName + " " + lastName + " added to database with id " + str(newId)


@app.route('/getCustomers')
def getCustomers():
    #jsonstr = storedb.getCustomers()
    jsonstr = '[{"id":"","first":"John","last":"Smith"}]'
    return jsonstr

@app.route('/getmsg')
def junk():
    return "Hello webpage"


# python flask-webserver.py
# http://localhost:5000/
# this loads the 'index.html' file in 'templates' directory

if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)
