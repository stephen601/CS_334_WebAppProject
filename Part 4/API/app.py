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
        ice_cream = [
            dict(ice_cream_id=row[0], name=row[1], price=row[2], image=row[3])
            for row in cursor.fetchall()
        ]

        if ice_cream:
            return jsonify(ice_cream)
        else:
            return f"No orders found for user with id: {id}", 404


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
        users = [
            dict(user_id=row[0], username=row[1], password=row[2], is_admin=row[3])
            for row in cursor.fetchall()
        ]

        if users:
            return jsonify(users)
        else:
            return f"No users found for user with id: {id}", 404


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

@app.route("/orders", methods=["GET", "POST"])
def orders():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM orders")
        orders = [
            dict(id=row[0], user_id=row[1], ice_cream_id=row[2], quantity=row[3])
            for row in cursor.fetchall()
        ]
        if orders is not None:
            return jsonify(orders)

    if request.method == "POST":
        user_id = request.form["user_id"]
        ice_cream_id = request.form["ice_cream_id"]
        quantity = request.form["quantity"]
        total_price = request.form["total_price"]
        order_date = request.form["order_date"]

        sql = """INSERT INTO orders (username_id, ice_cream_id, quantity, total_price, order_date)
                 VALUES (?,?,?,?,?)"""

        cursor = cursor.execute(sql, (user_id, ice_cream_id, quantity, total_price, order_date))
        conn.commit()
        return f"Order with id: {cursor.lastrowid} created successfully", 201

@app.route("/orders/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_order(id):
    conn = db_connection()
    cursor = conn.cursor()
    order = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM orders WHERE id=?", (id,))
        orders = [
            dict(order_id=row[0], ice_cream_id=row[1], user_id=row[2], quantity=row[3], total_price=row[4], order_date=row[5])
            for row in cursor.fetchall()
        ]

        if orders:
            return jsonify(orders)
        else:
            return f"No orders found for user with id: {id}", 404

    if request.method == "PUT":
        sql = """UPDATE orders
                SET user_id=?,
                    ice_cream_id=?,
                    quantity=?
                WHERE id=? """

        user_id = request.form["user_id"]
        ice_cream_id = request.form["ice_cream_id"]
        quantity = request.form["quantity"]
        updated_order = {
            "id": id,
            "user_id": user_id,
            "ice_cream_id": ice_cream_id,
            "quantity": quantity
        }
        conn.execute(sql, (user_id, ice_cream_id, quantity, id))
        conn.commit()
        return jsonify(updated_order)

    if request.method == "DELETE":
        sql = """ DELETE FROM orders WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "Order with id: {} has been deleted.".format(id), 200

@app.route("/orders/user/<int:username_id>", methods=["GET"])
def orders_by_user_id(username_id):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders WHERE username_id=?", (username_id,))
    orders = [
        dict(order_id=row[0], ice_cream_id=row[1], user_id=row[2], quantity=row[3], total_price=row[4], order_date=row[5])
        for row in cursor.fetchall()
    ]

    if orders:
        return jsonify(orders)
    else:
        return f"No orders found for user with id: {username_id}", 404


if __name__ == '__main__':
    app.run(debug=True)
