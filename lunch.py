from flask import Flask, jsonify, abort, request
from lunchDAO import lunchDAO
import datetime

app = Flask(__name__, static_url_path='', static_folder='static')

lunch_options = [
    {'name':'Chicken Salad'},
    {'name':'Ham and Cheese Sandwich'},
    {'name':'Chorizo Pasta'},
    {'name':'Tuna Melt'},
    {'name':'Soup and Bread'},
    {'name':'Vegtable Rizotto'},
    ]

'''
[
    {'name':'John Doe', 'handicap':10, 'dob':'1974-01-02', 'Score':'-2'},
    {'name':'Mary Black', 'handicap':16, 'dob':'1997-11-09', 'Score':'+1'},
    {'name':'Joe Joyce', 'handicap':7, 'dob':'1990-04-12', 'Score':'E'},
    ]


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT username,password FROM users WHERE username=%s", [username])
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

@app.route('/lunch', methods=['GET'])
def getAllLunches():
    return jsonify(lunch_options)


@app.route('/choice/<lunch_option>', methods=['POST'])
def addALunchOption(lunch_option):
    now = datetime.datetime.now()
    #student_id = request.form['student_id']
    #data = (lunch_option, student_id, now)
    data = (lunch_option, 'test', now)
    newid = lunchDAO.create(data)

    return jsonify({'id':newid})


@app.route('/choice/<lunch_option>', methods=['GET'])
def getCountForLunches(lunch_option):
    count = lunchDAO.countchoices(lunch_option)
    return jsonify({lunch_option:count})


@app.route('/choice', methods=['GET'])
def getAllCount():
    allcounts = []
    for lunch_option in lunch_options:
        lunch_option = lunch_option['name'] 
        count = lunchDAO.countchoices(lunch_option)
        allcounts.append({lunch_option:count})
    return jsonify(allcounts)


@app.route('/choice/all', methods=['delete'])
def deleteAllChoices():
    return jsonify({'done':True})



if __name__ == "__main__":
    app.run(debug=True)