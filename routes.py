from app import app
from flask import render_template, request, redirect
import users
import products
import receipts
import shops

@app.route("/")
def index():
    return render_template("index.html", receipts=receipts.get_all_receipts()) 

#Receipt block
@app.route("/add_receipt")
def add_receipt():
    return render_template("add_receipt.html", receipts=receipts.get_all_receipts()[1]) 


@app.route("/add_receipt", methods=["POST"])
def save_receipt():
    shop_name = request.form["shop_name"]
    shop_type = request.form["type"]
    date_issued = request.form["date"]

    shops.add_shop(shop_name, shop_type)
    receipts.save_receipt(shop_name, date_issued)
    return redirect("/add_receipt")


#product block
@app.route("/product")
def product():
    return render_template("product.html")


#@app.route("/add_product")
#def product():
    #product = request.form["name"]
    #price = request.form["price"]
    #type = request.form["type"]
    #calories = request.form["calories"]
   # products.add_product(product,price,type,calories)
    #return redirect("/add_receipt")

#User block
@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", wrong_login="Tili tai salasana on virheellinen.")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Tunnuksessa tulee olla 1-20 merkkiä")