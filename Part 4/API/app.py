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
        if ice_cream is not None:
            return jsonify(ice_cream), 200
        else:
            return "Something wrong", 404

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


if __name__ == '__main__':
    app.run(debug=True)
