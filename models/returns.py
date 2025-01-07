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

    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"), nullable=False)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"), nullable=False)
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_selling_price: Mapped[Float] = mapped_column(Float, nullable=False)
    total_price: Mapped[Float] = mapped_column(Float, nullable=False)
    amount_paid: Mapped[Float] = mapped_column(Float, nullable=False)
    payment_status: Mapped[str] = mapped_column(Enum("PAID", "UNPAID", "DEPOSIT"), nullable=False)
    payment_type: Mapped[str] = mapped_column(String(20), nullable=False)
    customer_id: Mapped[str] = mapped_column(ForeignKey("customers.id"), default="unknown")
    warehouse_id: Mapped[str] = mapped_column(ForeignKey("warehouses.id"), nullable=False)
    reason: Mapped[str] = mapped_column(String(100), nullable=True)
    employee_id: Mapped[str] = mapped_column(ForeignKey("employees.id"), nullable=False)



class ReturnOutward(BaseModel, Base):
    """
    Represents returns made to suppliers in Benrays store with
    product category, name, color, quantity, unit_cost_price,
    total_price, payment status, payment type, supplier, warehouse,
    reason, employee
    """
    __tablename__ = "return_outwards"

    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"), nullable=False)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"), nullable=False)
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_cost_price: Mapped[Float] = mapped_column(Float, nullable=False)
    total_price: Mapped[Float] = mapped_column(Float, nullable=False)
    amount_paid: Mapped[Float] = mapped_column(Float, nullable=False)
    payment_status: Mapped[str] = mapped_column(Enum("PAID", "UNPAID", "DEPOSIT"), nullable=False)
    payment_type: Mapped[str] = mapped_column(String(20), nullable=False)
    supplier_id: Mapped[str] = mapped_column(ForeignKey("suppliers.id"), default="unknown")
    warehouse_id: Mapped[str] = mapped_column(ForeignKey("warehouses.id"), nullable=False)
    reason: Mapped[str] = mapped_column(String(100), nullable=True)
    employee_id: Mapped[str] = mapped_column(ForeignKey("employees.id"), nullable=False)
