from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ice_cream.sqlite'
db = SQLAlchemy(app)

class IceCream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100))

class Usernames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Integer, default=0)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ice_cream_id = db.Column(db.Integer, db.ForeignKey('ice_cream.id'), nullable=False)
    username_id = db.Column(db.Integer, db.ForeignKey('usernames.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    ice_cream = db.relationship('IceCream', backref=db.backref('orders', lazy=True))
    username = db.relationship('Usernames', backref=db.backref('orders', lazy=True))

@app.route("/ice_cream", methods=["GET", "POST"])
def ice_cream():
    if request.method=="GET":
        ice_cream = IceCream.query.all()
        return jsonify([{"id": i.id, "name": i.name, "price": i.price, "image": i.image} for i in ice_cream])

    if request.method == "POST":
        new_name = request.form["name"]
        new_price = request.form["price"]
        new_image = request.form["image"]
        new_ice_cream = IceCream(name=new_name, price=new_price, image=new_image)
        db.session.add(new_ice_cream)
        db.session.commit()
        return f"Ice cream with id: {new_ice_cream.id} created successfully", 201

@app.route("/ice_cream/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_ice_cream(id):
    ice_cream = IceCream.query.get(id)
    if request.method == "GET":
        if ice_cream:
            return jsonify({"id": ice_cream.id, "name": ice_cream.name, "price": ice_cream.price, "image": ice_cream.image})
        else:
            return f"No ice cream found for id: {id}", 404

    if request.method == "PUT":
        if ice_cream:
            ice_cream.name = request.form["name"]
            ice_cream.price = request.form["price"]
            ice_cream.image = request.form["image"]
            db.session.commit()
            return jsonify({"id": ice_cream.id, "name": ice_cream.name, "price": ice_cream.price, "image": ice_cream.image})
        else:
            return f"No ice cream found for id: {id}", 404

    if request.method == "DELETE":
        if ice_cream:
            db.session.delete(ice_cream)
            db.session.commit()
            return f"Ice cream with id: {id} deleted successfully", 200
        else:
            return f"No ice cream found for id: {id}", 404

@app.route("/user", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        users = Usernames.query.all()
        return jsonify([{"id": u.id, "username": u.username, "is_admin": u.is_admin} for u in users])

    if request.method == "POST":
        new_username = request.form["username"]
        new_password = request.form["password"]
        new_is_admin = request.form.get("is_admin", False)
        new_user = Usernames(username=new_username, password=new_password, is_admin=new_is_admin)
        db.session.add(new_user)
        db.session.commit()
        return f"User with id: {new_user.id} created successfully", 201

@app.route("/user/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_user(id):
    user = Usernames.query.get(id)
    if request.method == "GET":
        if user:
            return jsonify({"id": user.id, "username": user.username, "is_admin": user.is_admin})
        else:
            return f"No user found for id: {id}", 404

    if request.method == "PUT":
        if user:
            user.username = request.form["username"]
            user.password = request.form["password"]
            user.is_admin = request.form.get("is_admin", user.is_admin)
            db.session.commit()
            return jsonify({"id": user.id, "username": user.username, "is_admin": user.is_admin})
        else:
            return f"No user found for id: {id}", 404

    if request.method == "DELETE":
        if user:
            db.session.delete(user)
            db.session.commit()
            return f"User with id: {id} deleted successfully", 200
        else:
            return f"No user found for id: {id}", 404

@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "GET":
        orders = Orders.query.all()
        return jsonify([{"id": o.id, "username_id": o.username_id, "ice_cream_id": o.ice_cream_id, "quantity": o.quantity, "total_price" : o.total_price, "order_date" : o.order_date} for o in orders])

    if request.method == "POST":
        username_id = request.form["username_id"]
        ice_cream_id = request.form["ice_cream_id"]
        quantity = request.form["quantity"]
        total_price = request.form["total_price"]
        order_date = request.form["order_date"]
        new_order = Orders(username_id=username_id, ice_cream_id=ice_cream_id, quantity=quantity,total_price=total_price, order_date=datetime.strptime(order_date, '%a, %d %b %Y %H:%M:%S %Z'))
        db.session.add(new_order)
        db.session.commit()
        return f"Order with id: {new_order.id} created successfully", 201

@app.route("/orders/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_order(id):
    order = Orders.query.get(id)
    if request.method == "GET":
        if order:
            return jsonify({
                "id": order.id,
                "ice_cream_id": order.ice_cream_id,
                "username_id": order.username_id,
                "quantity": order.quantity,
                "total_price": order.total_price,
                "order_date": order.order_date,
                "ice_cream": {
                    "id": order.ice_cream.id,
                    "name": order.ice_cream.name,
                    "price": order.ice_cream.price,
                    "image": order.ice_cream.image
                },
                "username": {
                    "id": order.username.id,
                    "username": order.username.username,
                    "is_admin": bool(order.username.is_admin)
                }
            })
        else:
            return f"No order found for id: {id}", 404

    if request.method == "PUT":
        if order:
            order.ice_cream_id = request.form["ice_cream_id"]
            order.username_id = request.form["username_id"]
            order.quantity = request.form["quantity"]
            order.total_price = request.form["total_price"]
            order.order_date = datetime.strptime(request.form["order_date"], '%a, %d %b %Y %H:%M:%S %Z')

            db.session.commit()
            return jsonify({
                "id": order.id,
                "ice_cream_id": order.ice_cream_id,
                "username_id": order.username_id,
                "quantity": order.quantity,
                "total_price": order.total_price,
                "order_date": order.order_date,
                "ice_cream": {
                    "id": order.ice_cream.id,
                    "name": order.ice_cream.name,
                    "price": order.ice_cream.price,
                    "image": order.ice_cream.image
                },
                "username": {
                    "id": order.username.id,
                    "username": order.username.username,
                    "is_admin": bool(order.username.is_admin)
                }
            })
        else:
            return f"No order found for id: {id}", 404

    if request.method == "DELETE":
        if order:
            db.session.delete(order)
            db.session.commit()
            return f"Order with id: {id} deleted successfully", 200
        else:
            return f"No order found for id: {id}", 404

@app.route("/orders/user/<int:username_id>", methods=["GET"])
def orders_by_user_id(username_id):
    orders = Orders.query.filter_by(username_id=username_id).all()
    orders_list = []

    for order in orders:
        order_dict = {
            "order_id": order.id,
            "ice_cream_id": order.ice_cream_id,
            "user_id": order.username_id,
            "quantity": order.quantity,
            "total_price": order.total_price,
            "order_date": order.order_date,
        }
        orders_list.append(order_dict)

    if orders_list:
        return jsonify(orders_list)
    else:
        return f"No orders found for user with id: {username_id}", 404

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
if __name__ == '__main__':
    app.run(debug=True)