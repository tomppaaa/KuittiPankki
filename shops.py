from db import db

#Module for adding shops.
def add_shop(name, type):
    sql = "INSERT INTO shops (shop_name, type) VALUES (:name,:type)"
    db.session.execute(sql, {"name":name, "type":type})
    db.session.commit()

    #Tänne tulee error handler.
