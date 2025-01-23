#!/usr/bin/python3
"""
This module contains classes for defining Products in
Benrays inventory management system.

classes:
    Category class: Defines the categories of products
    Product class: Defines the products
    Color class: Defines the colors of products
"""

from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Table, Column



product_color = Table(
                        "product_colors",
                        Base.metadata,
                        Column("product_id", ForeignKey("products.id"), primary_key=True),
                        Column("color_id", ForeignKey("colors.id"), primary_key=True)
                )


class Category(BaseModel, Base):
    """
    Defines the categories of products
    """
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(60), unique=True)
    products: Mapped[list["Product"]] = relationship(back_populates="category")
    


class Product(BaseModel, Base):
    """
    Creates a blueprint for products in Benrays inventory
    """
    __tablename__ = "products"
    name: Mapped[str] = mapped_column(String(60), unique=True)
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="products")
    colors: Mapped[list["Color"]] = relationship(secondary=product_color, back_populates="products")    



class Color(BaseModel, Base):
    """
    Defines the colors for the products in Benrays inventory
    """
    __tablename__ = "colors"
    name: Mapped[str] = mapped_column(String(60), unique=True)
    products: Mapped[list["Product"]] = relationship(secondary=product_color, back_populates="colors")
    
