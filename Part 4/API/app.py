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
    cursor = conn.cursor()

    if request.method=="GET":
        cursor.execute("SELECT * FROM ice_cream")

        ice_cream = [
            dict(id=row[0], name=row[1], price = row[2], image = row[3])
            for row in cursor.fetchall()
        ]
        if ice_cream is not None:
            return jsonify(ice_cream)

    if request.method == "POST":
        new_name = request.form["name"]
        new_price = request.form["price"]
        new_image = request.form["image"]

        sql = """INSERT INTO ice_cream (name, price, image)
                 VALUES (?,?,?)"""

        cursor = cursor.execute(sql, (new_name, new_price))
        conn.commit()
        return f"Ice creame with the id: {cursor.lastrowid} created sussessfully", 201

@app.route("/ice_cream/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_ice_cream(id):
    conn = db_connection()
    cursor = conn.cursor()
    ice_cream = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM ice_cream WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            ice_cream = r
        # if ice_cream is not None:
        #     return jsonify(ice_cream), 200
        # else:
        #     return "Something wrong", 404
        if ice_cream is not None:
            ice_cream = {"id": ice_cream[0], "name": ice_cream[1], "price": ice_cream[2], "image": ice_cream[3]}
            return jsonify(ice_cream)
        else:
            return jsonify({"message": "Ice cream not found"}), 404

    if request.method == "PUT":
        sql = """UPDATE ice_cream
                SET name=?,
                    price=?,
                    image=?
                WHERE id=? """

        name = request.form["name"]
        price = request.form["price"]
        image = request.form["image"]
        updated_ice_cream = {
            "id": id,
            "name": name,
            "price": price,
            "image": image
        }
        conn.execute(sql, (name, price, image, id))
        conn.commit()
        return jsonify(updated_ice_cream)

    if request.method == "DELETE":
        sql = """ DELETE FROM ice_cream WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The ice cream with id: {} has been deleted.".format(id), 200

@app.route("/users", methods=["GET", "POST"])
def users():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM usernames")
        users = [
            dict(id=row[0], username=row[1], password=row[2], is_admin=row[3])
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users)

    if request.method == "POST":
        new_username = request.form["username"]
        new_password = request.form["password"]
        is_admin = request.form.get("is_admin", default=0, type=int)

        sql = """INSERT INTO usernames (username, password, is_admin)
                 VALUES (?,?,?)"""

        cursor = cursor.execute(sql, (new_username, new_password, is_admin))
        conn.commit()
        return f"User with the id: {cursor.lastrowid} created successfully", 201

@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_user(id):
    conn = db_connection()
    cursor = conn.cursor()
    user = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM usernames WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            user = r
        # if user is not None:
        #     return jsonify(user), 200
        # else:
        #     return "User not found", 404
        if user is not None:
            user = {"id": user[0], "username": user[1], "password": user[2], "is_admin": user[3]}
            return jsonify(user)
        else:
            return jsonify({"message": "User not found"}), 404

    if request.method == "PUT":
        sql = """UPDATE usernames
                SET username=?,
                    password=?,
                    is_admin=?
                WHERE id=? """

        username = request.form["username"]
        password = request.form["password"]
        is_admin = request.form.get("is_admin", default=0, type=int)
        updated_user = {
            "id": id,
            "username": username,
            "password": password,
            "is_admin": is_admin
        }
        conn.execute(sql, (username, password, is_admin, id))
        conn.commit()
        return jsonify(updated_user)

    if request.method == "DELETE":
        sql = """ DELETE FROM usernames WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "User with id: {} has been deleted.".format(id), 200



if __name__ == '__main__':
    app.run(debug=True)
