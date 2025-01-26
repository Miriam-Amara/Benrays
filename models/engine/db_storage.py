#!/usr/bin/python3

"""
This module defines the DBStorage class, which provides methods to
interact with a database using SQLAlchemy. It handles database
connections, performs CRUD operations, and ensures data persistence.
"""

from models.base_model import BaseModel, Base
from models.products import Category, Product, product_color, Color
from models.warehouses import Warehouse, warehouse_product, warehouse_employee
from models.employees import Employee
from models.customers import Customer
from models.suppliers import Supplier
from models.inventory import Inventory
from models.inventory_transactions import InventoryTransaction
from models.sales import Sale
from models.purchases import Purchase
from models.orders import Order
from models.order_items import PurchaseOrder, CustomerOrder, TransferOrder
from models.returns import ReturnInward, ReturnOutward

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, select, func
from dotenv import load_dotenv
import os

load_dotenv()
db_user = os.getenv("BENRAYS_INVENTORY_MYSQL_USER")
passwd = os.getenv("BENRAYS_INVENTORY_MYSQL_PWD")
host = os.getenv("BENRAYS_INVENTORY_MYSQL_HOST")
port = os.getenv("BENRAYS_INVENTORY_MYSQL_PORT")
database = os.getenv("BENRAYS_INVENTORY_MYSQL_DATABASE")


db_url = f"mysql+mysqldb://{db_user}:{passwd}@{host}:{port}/{database}"


class DBStorage:
    """
    A class to manage storage of data in a database using SQLAlchemy.
    """

    __engine = None
    __session = None
    classes = [
        Category,
        Product,
        Color,
        Warehouse,
        Employee,
        Customer,
        Supplier,
        Inventory,
        InventoryTransaction,
        Sale,
        Purchase,
        Order,
        PurchaseOrder,
        CustomerOrder,
        TransferOrder,
        ReturnInward,
        ReturnOutward,
    ]

    def __init__(self):
        """initializes attributes for DBStorage objects"""
        self.__engine = create_engine(
            db_url,
            pool_pre_ping=True,
        )
        if os.getenv("DB_ENV") == "test":
            # parse the test database for testing to avoid
            # deletion of the actual database.
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns all objects or objects of the specified class from
        from the database.
        """
        all_objects = []
        objects_dict = {}
        if cls in DBStorage.classes:
            query = select(cls)
            cls_obj = self.__session.scalars(query).all()
            all_objects.extend(cls_obj)
        else:
            for clsname in DBStorage.classes:
                query = select(clsname)
                cls_obj = self.__session.scalars(query).all()
                all_objects.extend(cls_obj)

        for obj in all_objects:
            key = f"{obj.__class__.__name__}.{obj.id}"
            objects_dict[key] = obj

        return objects_dict

    def get(self, cls, id=None, name=None, email=None):
        """Returns the object that has the specified id or name"""
        obj_dict = {}
        obj = ""
        if id:
            query = select(cls).where(cls.id == id)
            obj = self.__session.scalars(query).one_or_none()
        elif name:
            query = select(cls).where(cls.name == name)
            obj = self.__session.scalars(query).one_or_none()
        elif email:
            query = select(cls).where(cls.email == email)
            obj = self.__session.scalars(query).one_or_none()

        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            obj_dict[key] = obj
            return obj_dict
        else:
            return None

    def count(self, cls=None):
        """
        Returns the total no of the given class objects in the database
        or the total no of all objects in the database if no class is given.
        """
        total_count = 0
        if cls in DBStorage.classes:
            query = select(func.count(cls.id))
            total_count = self.__session.scalars(query).first()
        else:
            for clsname in DBStorage.classes:
                query = select(func.count(clsname.id))
                total_count = (total_count +
                               self.__session.scalars(query).first())
        return total_count

    def new(self, obj):
        """Adds objects to database"""
        self.__session.add(obj)

    def save(self):
        """Saves objects to database"""
        try:
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()
            raise ValueError(f"Failed to commit: {e}")

    def reload(self):
        """Creates all tables and database session"""
        try:
            Base.metadata.create_all(self.__engine)
        except Exception as e:
            return
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )

    def delete(self, obj):
        """Deletes object from database"""
        self.__session.delete(obj)

    def close(self):
        """Closes database session"""
        self.__session.remove()


if __name__ == "__main__":
    storage = DBStorage()
    storage.reload()
