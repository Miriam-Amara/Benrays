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



ProductColor = Table(
                        "product_colors",
                        Base.metadata,
                        Column("product_id", ForeignKey("products.id"),
                               primary_key=True, nullable=False
                            ),
                        Column("color_id", ForeignKey("colors.id"),
                               primary_key=True, nullable=False
                            ),
                )



class Category(BaseModel, Base):
    """
    Defines the categories of products
    """
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    products: Mapped[list["Product"]] = relationship(back_populates="categories", cascade="all, delete-orphan")



class Product(BaseModel, Base):
    """
    Creates a blueprint for products in Benrays inventory
    """
    __tablename__ = "products"
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"), nullable=False)

    categories: Mapped["Category"] = relationship(back_populates="products")
    colors: Mapped[list["Color"]] = relationship(secondary=ProductColor, back_populates="products")
    



class Color(BaseModel, Base):
    """
    Defines the colors for the products in Benrays inventory
    """
    __tablename__ = "colors"
    name: Mapped[str] = mapped_column(String(60), nullable=False)

    products: Mapped[list["Product"]] = relationship(secondary=ProductColor, back_populates="colors")
