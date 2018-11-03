from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def render():
   return render_template('index.html')

@app.route('/addCustomer')
def render_html_template():
   return render_template('customer-input.html')

@app.route('/addCustomerToDB')
def addCustomerToDB():
    firstName = request.args.get('firstName', 'unknown')
    lastName = request.args.get('lastName', 'unknown')
    print( "firstName:" + firstName + ",lastName:" + lastName)
    return firstName + " " + lastName + " added to database"

@app.route('/getmsg')
def junk():
    return "Hello webpage"

@app.route('/getgreeting')
def greeting():
    name = request.args.get('name', 'unknown')
    if len(name) == 0:
       name = "unknown"
    return "Hello " + name

# python flask-webserver.py
# http://localhost:5000/
# this loads the 'index.html' file in 'templates' directory

if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)
