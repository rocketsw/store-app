from flask import Flask, render_template, redirect, url_for
from flask import request
from flask import jsonify
from StoreDB import StoreDB
import json

app = Flask(__name__)
storedb = StoreDB()

@app.route('/')
def render():
   return render_template('index.html')

@app.route('/example.html')
def render_example():
   return render_template('example.html')

@app.route('/table.html')
def render_table():
   return render_template('table.html')

@app.route('/main.html')
def render_main():
   return render_template('main.html')

@app.route('/customers.html')
def render_customers():
   return render_template('customers.html')

@app.route('/customeradd.html')
def render_customer_input():
   return render_template('customeradd.html')

@app.route('/customeredit.html')
def render_customer_edit():
    id = request.args.get('id', 'unknown')
    first = request.args.get('first', 'unknown')
    last = request.args.get('last', 'unknown')
    street = request.args.get('street', 'unknown')
    city = request.args.get('city', 'unknown')
    state = request.args.get('state', 'unknown')
    zip = request.args.get('zip', 'unknown')
    phone = request.args.get('phone', 'unknown')
    #jsonStr = '{"id":"' + id + '","first":"' + first + '","last":"' + last + '","street":"' + street + '","city":"' + city + '","state":"' + state + '","zip":"' + zip + '","phone":"' + phone + '"}'
    jsonObj = {"id":id,"first":first,"last":last,"street":street,"city":city,"state":state,"zip":zip,"phone":phone}
    #print( "jsonObj: " + str(jsonObj) )
    jsonStr = json.dumps( jsonObj )
    #print( "jsonStr: " + jsonStr )
    return render_template('customeredit.html', data = jsonObj )

@app.route('/addCustomerToDB')
def addCustomerToDB():
    first = request.args.get('first', 'unknown')
    last = request.args.get('last', 'unknown')
    street = request.args.get('street', 'unknown')
    city = request.args.get('city', 'unknown')
    state = request.args.get('state', 'unknown')
    zip = request.args.get('zip', 'unknown')
    phone = request.args.get('phone', 'unknown')
    jsonstr = '{"first":"' + first + '","last":"' + last + '","street":"' + street + '","city":"' + city + '","state":"' + state + '","zip":"' + zip + '","phone":"' + phone + '"}'
    print( jsonstr )
    newId = storedb.insertCustomer( jsonstr )
    newId = 6
    return first + " " + last + " " + street + " " + city + " " + state + " " + zip + " " + phone + " added to database with id " + str(newId)

@app.route('/updateCustomer')
def updateCustomer():
    id = request.args.get('id', 'unknown')
    first = request.args.get('first', 'unknown')
    last = request.args.get('last', 'unknown')
    street = request.args.get('street', 'unknown')
    city = request.args.get('city', 'unknown')
    state = request.args.get('state', 'unknown')
    zip = request.args.get('zip', 'unknown')
    phone = request.args.get('phone', 'unknown')
    jsonstr = '{"id":"' + id + '","first":"' + first + '","last":"' + last + '","street":"' + street + '","city":"' + city + '","state":"' + state + '","zip":"' + zip + '","phone":"' + phone + '"}'
    print( jsonstr )
    id = storedb.updateCustomer( jsonstr )
    return id

@app.route('/editCustomer')
def editCustomer():
    print("inside editCustomer")
    id = request.args.get('id', 'unknown')
    first = request.args.get('first', 'unknown')
    last = request.args.get('last', 'unknown')
    street = request.args.get('street', 'unknown')
    city = request.args.get('city', 'unknown')
    state = request.args.get('state', 'unknown')
    zip = request.args.get('zip', 'unknown')
    phone = request.args.get('phone', 'unknown')
    print("id=" + id)
    retobj = {"id":id,"first":first,"last":last,"street":street,"city":city,"state":state,"zip":zip,"phone":phone}
    jsonstr = '{"id":"' + id + '","first":"' + first + '","last":"' + last + '","street":"' + street + '","city":"' + city + '","state":"' + state + '","zip":"' + zip + '","phone":"' + phone + '"}'
    print( "jsonstr=")
    print( jsonstr )
    jsonObj = json.dumps(jsonstr)
    print( "did json.dumps")
    print( jsonObj )
    #print( url_for('/customeredit.html'))
    return redirect(url_for('render_customer_edit'))

@app.route('/getCustomers')
def getCustomers():
    jsonstr = storedb.getCustomers()
    return jsonstr

@app.route('/getmsg')
def junk():
    return "Hello webpage"


# python flask-webserver.py
# http://localhost:5000/
# this loads the 'index.html' file in 'templates' directory

if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)
