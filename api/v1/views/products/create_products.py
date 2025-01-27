#!/usr/bin/python3

"""
This module implements route for
creating new categories, products and
colors. Adding them to database.
"""

from models import storage
from models.products import Category, Product, Color
from api.v1.views.products import products_bp

from flask_restful import Api, reqparse, Resource, abort

api = Api(products_bp)

category_args = reqparse.RequestParser()
product_args = reqparse.RequestParser()
color_args = reqparse.RequestParser()

category_args.add_argument(
    "name", type=str, required=True, help="Category name is required"
)

product_args.add_argument(
    "name", type=str, required=True, help="Product name is required"
)
product_args.add_argument(
    "category_id", type=str, required=True,
    help="Product Category id is required"
)

color_args.add_argument(
    "name", type=str, required=True, help="Product color name is required"
)


class CreateCategory(Resource):
    """
    This class provides post method for adding
    category to the database.
    """

    def post(self):
        """
        Checks wether a category already exists.
        Creates and add the category to database.
        """
        args = category_args.parse_args()
        category_name = args.get("name")

        # checks the value of category name is not None
        if category_name is None:
            abort(400, description="Category name cannot be None")

        # check that category is not in the database
        category_exists = storage.get(Category, name=category_name)
        if category_exists:
            abort(
                409,
                description=(f"{args['name']}"
                             " category already exists in the database"),
            )

        # creates the category and add to database
        new_category = Category(**args)
        new_category.save()

        # convert new_category to dictionary
        category_dict = new_category.to_dict()
        del category_dict["__class__"]

        return category_dict, 201


class CreateProduct(Resource):
    """
    This class provides post method for adding
    product to the database.
    """

    def post(self):
        """
        Checks wether a product already exists.
        Creates and add the product to database.
        """
        args = product_args.parse_args()
        product_name = args.get("name")
        category_id = args.get("category_id")

        # checks the value of pproduct name is not None
        if product_name is None or category_id is None:
            abort(400, description="Product name cannot be None")

        # check that product is not in the database
        product_exists = storage.get(Product, name=product_name)
        if product_exists:
            abort(
                409,
                description=f"{args['name']}"
                " product already exists in the database",
            )

        # creates the product and add to database
        new_product = Product(**args)
        new_product.save()

        # convert new_product to dictionary
        product_dict = new_product.to_dict()
        del product_dict["__class__"]

        return product_dict, 201


class CreateColor(Resource):
    """
    This class provides post method for adding
    colors to the database.
    """

    def post(self):
        """
        Checks wether a color already exists.
        Create and add the color to database.
        """
        args = color_args.parse_args()
        color_name = args.get("name")

        # checks the value of color name is not None
        if color_name is None:
            abort(400, description="Color name cannot be None")

        # check that the color is not in database
        color_exists = storage.get(Color, name=color_name)
        if color_exists:
            abort(
                409,
                description=f"{args['name']}"
                " color already exists in the database"
            )

        # creates the color and add to database
        new_color = Color(**args)
        new_color.save()

        # convert new_color to dictionary
        color_dict = new_color.to_dict()
        del color_dict["__class__"]

        return color_dict, 201


api.add_resource(CreateCategory, "/category/register")
api.add_resource(CreateProduct, "/register")
api.add_resource(CreateColor, "/color/register")
