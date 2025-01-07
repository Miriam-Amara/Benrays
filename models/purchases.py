#!/usr/bin/python3

"""
This module provides Purchase class for purchases made in
Benrays inventory management system
"""

from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, String, Integer, Float, ForeignKey


class Purchase(BaseModel, Base):
    """
    Represents purchases made in Benrays store with
    product category, name, color, quantity, unit_cost_price,
    total_price, supplier, warehouse, payment status, payment type,
    purchase_order_id, employee
    """
    __tablename__ = "purchases"

    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"), nullable=False)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"), nullable=False)
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_cost_price: Mapped[Float] = mapped_column(Float, nullable=False)
    total_price: Mapped[Float] = mapped_column(Float, nullable=False)
    amount_paid: Mapped[Float] = mapped_column(Float, nullable=False)
    payment_status: Mapped[str] = mapped_column(Enum("PAID", "UNPAID", "DEPOSIT"), nullable=False)
    payment_type: Mapped[str] = mapped_column(String(20), nullable=False)
    supplier_id: Mapped[str] = mapped_column(ForeignKey("suppliers.id"),
                                             nullable=False, default="unknown"
                                        )
    warehouse_id: Mapped[str] = mapped_column(ForeignKey("warehouses.id"), nullable=False)
    purchase_order_id: Mapped[str] = mapped_column(ForeignKey("purchase_orders.id"), nullable=True)
    employee_id: Mapped[str] = mapped_column(ForeignKey("employees.id"), nullable=False)