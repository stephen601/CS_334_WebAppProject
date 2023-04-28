from flask import Flask, make_response, jsonify, request
import json
import sqlite3


app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('ice_cream.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/ice_cream", methods=["GET", "POST"])
def ice_cream():
    conn = db_connection()
    cursor = conn.execute("SELECT * FROM ice_cream")
    ice_cream = [
        dict(id=row[0], name=row[1], price = row[2])
        for row in cursor.fetchall()
    ]
    if ice_cream is not None:
        return jsonify(ice_cream)

# @app.route('/')
# def hello():
#     return 'Hello World!'

# table = db['ice_cream']


# def fetch_db(ice_cream_id):  # Each book scnerio
#     return table.find_one(ice_cream_id=ice_cream_id)


# def fetch_db_all():
#     ice_cream = []
#     for ice_cream in table:
#         ice_cream.append(ice_cream)
#     return ice_cream


# @app.route('/api/db_populate', methods=['GET'])
# def db_populate():
#     table.insert({
#         "ice_cream_id": "1",
#         "name": "Vinilla",
#         "price": 5.99
#     })

#     table.insert({
#         "ice_cream_id": "2",
#         "name": "Chocolate",
#         "price": 2.00
#     })

#     return make_response(jsonify(fetch_db_all()),
#                          200)


# @app.route('/api/ice_cream', methods=['GET', 'POST'])
# def api_ice_cream():
#     if request.method == "GET":
#         return make_response(jsonify(fetch_db_all()), 200)
#     elif request.method == 'POST':
#         content = request.json
#         ice_cream_id = content['ice_cream']
#         table.insert(content)
#         return make_response(jsonify(fetch_db(ice_cream_id)), 201)  # 201 = Created


# @app.route('/api/ice_cream/<ice_cream_id>', methods=['GET', 'PUT', 'DELETE'])
# def api_each_ice_cream(ice_cream_id):
#     if request.method == "GET":
#         ice_cream_obj = fetch_db(ice_cream_id)
#         if ice_cream_obj:
#             return make_response(jsonify(ice_cream_obj), 200)
#         else:
#             return make_response(jsonify(ice_cream_obj), 404)
#     elif request.method == "PUT":  # Updates the ice cream
#         content = request.json
#         table.update(content, ['ice_cream_id'])

#         book_obj = fetch_db(ice_cream_id)
#         return make_response(jsonify(ice_cream_obj), 200)
#     elif request.method == "DELETE":
#         table.delete(id=ice_cream_id)

#         return make_response(jsonify({}), 204)



if __name__ == '__main__':
    app.run(debug=True)