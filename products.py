from db import db

#metodi tuotteen lisäämiseen.

def add_product(name, price, calories, type):
    sql = "INSERT INTO products (name, price, calories, type) VALUES (:name, :price, :calories, :type)"
    #receipt_id = select from count
    db.session.execute(sql, {"name":name,"price":price,"calories":calories,"type":type })
    db.session.commit()


    