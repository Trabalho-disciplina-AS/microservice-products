from flask import request, jsonify
from products.services.product_service import insert_product, get_product_by_id, get_image_by_id
from flask_restful import Resource
from products import app, api
import json
 

'''
{
    "qtd_random": 3,
    "only_discount": true
}
'''
class ProductImageController(Resource):
    def get(self, _id):
        product_image = get_image_by_id(_id)
        return product_image.read()


class ProductOneIDController(Resource):
    def get(self, _id):
        product = get_product_by_id(_id)
        product = json.loads(product.to_json())
        return product, 200

    def post(self):
        data_json = {
            "name": request.form["name"],
            "category": request.form["category"],
        }
        product_id = insert_product(data_json, request.files["image"])
        return jsonify({"_id": product_id}), 200


class ProductOneCategoryController(Resource):
    def post(self):
        data_json = {
            "name": request.form["name"],
            "category": request.form["category"],
        }
        product_id = insert_product(data_json, request.files["image"])
        return jsonify({"_id": product_id}), 200

api.add_resource(ProductOneIDController, "/product/<_id>")
api.add_resource(ProductImageController, "/product_image/<_id>")
api.add_resource(ProductOneCategoryController, "/product/<category>")
