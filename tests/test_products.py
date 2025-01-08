#!/usr/bin/python3

"""
This module provides unit tests for Product class.
"""

from models.products import Product, Category, Color
import unittest


class TestProduct(unittest.TestCase):
    """
    Defines test cases for the Product class attributes and methods.
    """
    def test_has_attributes(self):
        """
        Test that object of Product class inherits from BaseModel
        and contains its own attributes
        """
        self.product = Product()
        self.assertTrue(hasattr(self.product, "id"))
        self.assertTrue(hasattr(self.product, "created_at"))
        self.assertTrue(hasattr(self.product, "updated_at"))
        self.assertTrue(hasattr(self.product, "name"))
        self.assertTrue(hasattr(self.product, "category_id"))
        self.assertTrue(hasattr(self.product, "save"))
        self.assertTrue(hasattr(self.product, "__str__"))
    
    def test_save(self):
        """ Confirms objects are saved to database """
        category = Category(name="ccc")
        product1 = Product(name="hhhh", category_id=category.id)
        product2 = Product(name="wwww", category_id=category.id)
        product3 = Product(name="dddd", category_id=category.id)
        color1 = Color(name="black")
        color2 = Color(name="green")
        category.save()
        product1.save()
        product2.save()
        product3.save()
        color1.save()
        color2.save()
        product1.colors.append(color1)
        product1.colors.append(color2)
        from models import storage
        storage.save()
    
    def test_to_dict(self):
        """ 
        Confirms that a dictionary representation of the object
        is returned.
        """
        category = Category(name="hyrfdd")
        product = Product(name="uytrrr", category_id=category.id)

        obj_dict = product.to_dict()
        self.assertIn("__class__", obj_dict)
        



class TestCategory(unittest.TestCase):
    """
    Defines test cases for the Category class attributes and methods.
    """
    def test_has_attributes(self):
        """
        Test that object of Category class inherits from BaseModel
        and contains its own attributes
        """
        self.category = Category()
        self.assertTrue(hasattr(self.category, "id"))
        self.assertTrue(hasattr(self.category, "created_at"))
        self.assertTrue(hasattr(self.category, "updated_at"))
        self.assertTrue(hasattr(self.category, "name"))
        self.assertTrue(hasattr(self.category, "save"))
        self.assertTrue(hasattr(self.category, "__str__"))

    def test_save(self):
        """ Confirms objects are saved to database """
        category1 = Category(name="aaa")
        category2 = Category(name="bbb")
        category1.save()
        category2.save()



class TestColor(unittest.TestCase):
    """
    Defines test cases for the Color class attributes and methods.
    """
    def test_has_attributes(self):
        """
        Test that object of Color class inherits from BaseModel
        and contains its own attributes
        """
        self.color = Color()
        self.assertTrue(hasattr(self.color, "id"))
        self.assertTrue(hasattr(self.color, "created_at"))
        self.assertTrue(hasattr(self.color, "updated_at"))
        self.assertTrue(hasattr(self.color, "name"))
        self.assertTrue(hasattr(self.color, "save"))
        self.assertTrue(hasattr(self.color, "__str__"))

    def test_save(self):
        """ Confirms objects are saved to database """
        color1 = Color(name="ash")
        color2 = Color(name="blue")
        color1.save()
        color2.save()





if __name__ == "__main__":
    unittest.main(verbosity=2)