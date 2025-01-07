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

    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"), nullable=False)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"), nullable=False)
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"), nullable=False)
    warehouse_id: Mapped[str] = mapped_column(ForeignKey("warehouses_id"), nullable=False)
    transaction_type: Mapped[str] = mapped_column(
        Enum("IN", "OUT", "TRANSFER_IN", "TRANSFER_OUT", "RETURNED_IN", "RETURNED_OUT"),
        nullable=False
    )
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    source: Mapped[str] = mapped_column(
        Enum("PURCHASES", "SALES", "TRANSFERS", "RETURNS"), nullable=False
    )
    employee_id: Mapped[str] = mapped_column(ForeignKey("employees.id"), nullable=False)
    
