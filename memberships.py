from flask import Flask, jsonify, request, abort, render_template, session, g, redirect, url_for, flash
from membershipDAO import membershipDAO

app = Flask(__name__, static_url_path='', static_folder='templates')


@app.route('/login', methods=['GET', 'POST'])
def login():
    result = membershipDAO.testLogin()
    if result==2:
        flash('Invalid Username or Password !!')
        return render_template('login.html')
        
    else:
        return render_template('index.html')

    #return redirect("http://127.0.0.1:5000/login.html")

'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    users = membershipDAO.getAllUsers()
    users = jsonify(users)
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user    
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        #users = membershipDAO.getAllUsers()
        #users = jsonify(users)
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect("http://127.0.0.1:5000/index.html")

        return redirect("http://127.0.0.1:5000/login.html")

    return redirect("http://127.0.0.1:5000/login.html")
'''
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        cur = membershipDAO.cursor(membershipDAO.cursors.DictCursor)
        cur.execute("SELECT username, password FROM login_details WHERE username = %s", [username])
        user = cur.fetchone()
        if user:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = user['username']
            return render_template('lunch_choice.html', username=username)
        
        else:
            flash('Invalid Username or Password !!')
            return render_template('login.html')
    else:
        return render_template('login.html')
'''

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

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"hello\",\"membership_type\":\"someone\",\"email\":123}" http://127.0.0.1:5000/memberships
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

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"hello\",\"membership_type\":\"someone\",\"email\":123}" http://127.0.0.1:5000/memberships/1
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




if __name__ == '__main__' :
    app.run(debug= True)