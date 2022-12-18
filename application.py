from flask import Flask, jsonify, abort, request
from compDAO import compDAO

app = Flask(__name__, static_url_path='', static_folder='static')

golfers = [
    {'name':'John Doe', 'handicap':10, 'dob':19/10/1994, 'AM/PM':'AM'},
    {'name':'Mary Black', 'handicap':10, 'dob':19/10/1994, 'AM/PM':'AM'},
    {'name':'Joe Joyce', 'handicap':10, 'dob':19/10/1994, 'AM/PM':'AM'},
    ]

@app.route('/golfer', methods=['GET'])
def getAllGolfers():
    return jsonify(golfers)


@app.route('/competition/<golfername>', methods=['POST'])
def voteForBand(golfername):
    ip_addr = request.remote_addr
    data = (golfername, ip_addr)
    newid = compDAO.create(data)

    return jsonify({'id':newid})


@app.route('/competition/<golfername>', methods=['GET'])
def getCountForGolfers(golfername):
    count = compDAO.countgolfers(golfername)
    return jsonify({golfername:count})


@app.route('/competition', methods=['GET'])
def getAllCount():
    allcounts = []
    for golfer in golfers:
        golfername = golfer['name'] 
        count = compDAO.countgolfers(golfername)
        allcounts.append({golfername:count})
    return jsonify(allcounts)


@app.route('/competition/all', methods=['delete'])
def deleteAllGolfers():
    return jsonify({'done':True})



if __name__ == "__main__":
    app.run(debug=True)