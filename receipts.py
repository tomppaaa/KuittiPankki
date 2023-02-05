from db import db

#Module for getting total amount of receipts.
def get_all_receipts():
    result = db.session.execute("SELECT id FROM receipts")
    receipts = result.fetchall()
    return [len(receipts),receipts]

#Module for saving receipts.
def save_receipt(name, date):
    sql = "INSERT INTO receipts (shop_id, date_issued) SELECT id, :date FROM shops S WHERE :name = S.shop_name"
    db.session.execute(sql, {"name":name, "date":date})
    db.session.commit()

