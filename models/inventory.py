#!/usr/bin/python3

"""
This module provides Inventory class for
Benrays inventory management system
"""

from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey

class Inventory(BaseModel, Base):
    """"
    Represents an inventory with product category, product name,
    product color, quantity and warehouse name.
    """
    __tablename__ = "inventory"

    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"), nullable=False)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"), nullable=False)
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    warehouse_id: Mapped[str] = mapped_column(ForeignKey("warehouses.id"), nullable=False)
