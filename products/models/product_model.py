from products import db
from datetime import datetime


class Product(db.Document):
    meta = {"collection": "product"}
    name = db.StringField(required=False)
    price = db.FloatField(required=False)
    discount_price = db.FloatField(required=False)
    discount = db.BooleanField(required=False)
    category = db.StringField(max_length=50, required=False)
    image = db.FileField(required=False)
    created_at = db.DateTimeField(default=datetime.utcnow(), required=False)
    qtd_stock = db.IntField(required=False)
