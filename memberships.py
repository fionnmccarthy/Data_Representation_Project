from flask import Flask, jsonify, request, abort
from membershipDAO import membershipDAO

app = Flask(__name__, static_url_path='', static_folder='static')



#curl "http://127.0.0.1:5000/memberships"
@app.route('/memberships')
def getAll():
    #print("in getall")
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