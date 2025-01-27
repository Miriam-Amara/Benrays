#!/usr/bin/python3

"""
This module implements route for
updating existing categories, products and
colors. Adding their new values to database.
"""

from models import storage
from models.products import Category, Product, Color
from api.v1.views.products import products_bp

from flask_restful import Api, reqparse, Resource, abort

api = Api(products_bp)

category_args = reqparse.RequestParser()
product_args = reqparse.RequestParser()
color_args = reqparse.RequestParser()

category_args.add_argument("name", type=str)
product_args.add_argument("name", type=str)
product_args.add_argument("category_id", type=str)
color_args.add_argument("name", type=str)


class UpdateCategory(Resource):
    """
    This class provides put method for updating
    category in database.
    """

    def put(self, id):
        """
        Checks wether a category already exists.
        Updates its value in database.
        """
        args = category_args.parse_args()
        category_name = args.get("name")

        if not id:
            abort(400, description="Category id cannot be None/Null")

        if "name" in args and not category_name:
            abort(400, description="Category name cannot be empty")

        # get category from database
        id_exists = storage.get(Category, id=id)
        if not id_exists:
            abort(404, description=f"Category with id {id} not found")
        category = list(id_exists.values())[0]

        # updates the category name if it is different
        if category_name and category_name != category.name:
            name_exists = storage.get(Category, name=category_name)
            if name_exists:
                abort(400, description=f"{category_name} already exists")
            category.name = category_name
            category.save()

        category_data = category.to_dict()
        category_data.pop("__class__", None)

        return category_data, 200


class UpdateProduct(Resource):
    """
    This class provides put method for updating
    product in database.
    """

    def put(self, id):
        """
        Checks wether a product already exists.
        Updates its value in database.
        """
        args = product_args.parse_args()
        product_name = args.get("name")
        category_id = args.get("category_id")

        if not id:
            abort(400, description="Product id cannot be None/Null")

        # get the product obj from database
        product_dict = storage.get(Product, id=id)
        if not product_dict:
            abort(404, description=f"Product with id {id} not found")
        product = list(product_dict.values())[0]

        # updates the name or category_id if it is different
        if product_name and product_name != product.name:
            name_exists = storage.get(Product, name=product_name)
            if name_exists:
                abort(400, description=f"{product_name} already exists")
            product.name = product_name
        if category_id and category_id != product.category_id:
            id_exists = storage.get(Category, id=category_id)
            if not id_exists:
                abort(
                    404,
                    description=(f"product category id {id}"
                                 " not found in database")
                )
            product.category_id = category_id
        product.save()

        product_data = product.to_dict()
        product_data.pop("__class__", None)

        return product_data, 200


class UpdateColor(Resource):
    """
    This class provides put method for updating
    color in database.
    """

    def put(self, id):
        """
        Checks wether a color already exists.
        Updates its value in database.
        """
        args = color_args.parse_args()
        color_name = args.get("name")

        if not id:
            abort(400, description="Color id cannot be None/Null")

        if "name" in args and not color_name:
            abort(400, description="Color name cannot be empty")

        # get color from database
        id_exists = storage.get(Color, id=id)
        if not id_exists:
            abort(404, description=f"Color with id {id} not found")
        color = list(id_exists.values())[0]

        # updates the color name if it is different
        if color_name and color_name != color.name:
            name_exists = storage.get(Color, name=color_name)
            if name_exists:
                abort(400, description=f"{color_name} already exists")
            color.name = color_name
            color.save()

        color_data = color.to_dict()
        color_data.pop("__class__", None)

        return color_data, 200


api.add_resource(UpdateCategory, "/category/update/<id>")
api.add_resource(UpdateProduct, "/update/<id>")
api.add_resource(UpdateColor, "/color/update/<id>")
