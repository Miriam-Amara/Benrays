#!/usr/bin/python3

"""
This module provides InventoryTransaction class for
Benrays inventory management system
"""

from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, Integer, ForeignKey

class InventoryTransaction(BaseModel, Base):
    """"
    Represents the history of inventory movements in Benrays with
    product category, name, color, warehouse, transaction_type,
    quantity, source and employee.
    """
    __tablename__ = "inventory_transactions"

    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"))
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"))
    warehouse_id: Mapped[str] = mapped_column(ForeignKey("warehouses.id"))
    transaction_type: Mapped[str] = mapped_column(
        Enum("IN", "OUT", "TRANSFER_IN", "TRANSFER_OUT", "RETURNED_IN", "RETURNED_OUT"),

    )
    quantity: Mapped[int] = mapped_column(Integer)
    source: Mapped[str] = mapped_column(
        Enum("PURCHASES", "SALES", "TRANSFERS", "RETURNS")
    )
    employee_id: Mapped[str] = mapped_column(ForeignKey("employees.id"))
    
