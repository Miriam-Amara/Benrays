#!/usr/bin/python3

"""
This module provides Order class for orders in
Benrays inventory management system
"""

from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum


class Order(BaseModel, Base):
    """
    Represents orders for products in Benrays with
    orders status and emplyee name
    """
    __tablename__ = "orders"

    order_status: Mapped[str] = mapped_column(String(20))
    payment_status: Mapped[str] = mapped_column(
                                                Enum("paid", "unpaid", "deposit"))
    payment_methods: Mapped[str] = mapped_column(String(150))
