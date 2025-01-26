#!/usr/bin/python3

"""
This module provides ReturnInward class and ReturnOutward class
for goods return in Benrays inventory management system
"""

from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, String, Integer, Float, ForeignKey


class ReturnInward(BaseModel, Base):
    """
    Represents returns made by customers in Benrays store with
    product category, name, color, quantity, unit_selling_price,
    total_price, payment status, payment type, customer, warehouse,
    reason, employee
    """

    __tablename__ = "return_inwards"

    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"))
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    unit_selling_price: Mapped[Float] = mapped_column(Float)
    total_price: Mapped[Float] = mapped_column(Float)
    amount_paid: Mapped[Float] = mapped_column(Float)
    payment_status: Mapped[str] = mapped_column(
        Enum("paid", "unpaid", "deposit")
    )
    payment_type: Mapped[str] = mapped_column(String(20))
    customer_id: Mapped[str] = mapped_column(
        ForeignKey("customers.id"), default="unknown"
    )
    warehouse_id: Mapped[str] = mapped_column(ForeignKey("warehouses.id"))
    reason: Mapped[str] = mapped_column(String(100), nullable=True)
    employee_id: Mapped[str] = mapped_column(ForeignKey("employees.id"))


class ReturnOutward(BaseModel, Base):
    """
    Represents returns made to suppliers in Benrays store with
    product category, name, color, quantity, unit_cost_price,
    total_price, payment status, payment type, supplier, warehouse,
    reason, employee
    """

    __tablename__ = "return_outwards"

    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"))
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    unit_cost_price: Mapped[Float] = mapped_column(Float)
    total_price: Mapped[Float] = mapped_column(Float)
    amount_paid: Mapped[Float] = mapped_column(Float)
    payment_status: Mapped[str] = mapped_column(
        Enum("PAID", "UNPAID", "DEPOSIT")
    )
    payment_type: Mapped[str] = mapped_column(String(20))
    supplier_id: Mapped[str] = mapped_column(
        ForeignKey("suppliers.id"), default="unknown"
    )
    warehouse_id: Mapped[str] = mapped_column(ForeignKey("warehouses.id"))
    reason: Mapped[str] = mapped_column(String(100), nullable=True)
    employee_id: Mapped[str] = mapped_column(ForeignKey("employees.id"))
