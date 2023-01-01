from flask import Flask, jsonify, request, abort, render_template, session, g, redirect, url_for, flash
import json
import requests
import tabulate
from membershipDAO import membershipDAO

app = Flask(__name__, static_url_path='', static_folder='templates')


# start page for app
@app.route('/')
def initial():
    return render_template('/login.html')


@app.route('/login')
def login_page():
	return render_template('login.html')


# admin for members
@app.route('/admin')
def admin():
    return render_template('/index.html')

# fixtures page
@app.route('/fixtures2122')
def fixtures():
    return render_template('/fixtures.html')


# validate login details from database
@app.route('/login', methods = ['GET', 'POST'])
def login():
    users = membershipDAO.getAllUsers()
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        for dbuser in users: 
            if dbuser['username'] == username:
                if dbuser['password'] == password:
                    return render_template('index.html')
        else: 
            return render_template("login.html")     

    return render_template("login.html")


#curl "http://127.0.0.1:5000/user_logins"
@app.route('/userlogins')
def getAllUsers():
    results = membershipDAO.getAllUsers()
    return jsonify(results)


#curl "http://127.0.0.1:5000/memberships"
@app.route('/memberships')
def getAll():
    results = membershipDAO.getAll()
    return jsonify(results)


#curl "http://127.0.0.1:5000/memberships/2"
@app.route('/memberships/<int:id>')
def findById(id):
    foundmembership = membershipDAO.findByID(id)

    return jsonify(foundmembership)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"Tim Ryan\",\"membership_type\":\"gold\",\"email\":hello@live.ie}" http://127.0.0.1:5000/memberships
@app.route('/memberships', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    membership = {
        "name": request.json['name'],
        "membership_type": request.json['membership_type'],
        "email": request.json['email'],
    }
    values =(membership['name'],membership['membership_type'],membership['email'])
    newId = membershipDAO.create(values)
    membership['id'] = newId
    return jsonify(membership)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"Tim Ryan\",\"membership_type\":\"gold\",\"email\":hello2@live.ie}" http://127.0.0.1:5000/memberships/1
@app.route('/memberships/<int:id>', methods=['PUT'])
def update(id):
    foundmembership = membershipDAO.findByID(id)
    if not foundmembership:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'email' in reqJson and type(reqJson['email']) is not int:
        abort(400)

    if 'name' in reqJson:
        foundmembership['name'] = reqJson['name']
    if 'membership_type' in reqJson:
        foundmembership['membership_type'] = reqJson['membership_type']
    if 'email' in reqJson:
        foundmembership['email'] = reqJson['email']
    values = (foundmembership['name'],foundmembership['membership_type'],foundmembership['email'],foundmembership['id'])
    membershipDAO.update(values)
    return jsonify(foundmembership)
        

    

@app.route('/memberships/<int:id>' , methods=['DELETE'])
def delete(id):
    membershipDAO.delete(id)
    return jsonify({"done":True})


#curl "http://127.0.0.1:5000/fixturesdata"
@app.route('/fixturesdata')
def getFixtures():
    fixtures = requests.get('https://fixturedownload.com/feed/json/epl-2021/man-utd').json()
    return jsonify(fixtures)



if __name__ == '__main__' :
    app.run(debug= True)