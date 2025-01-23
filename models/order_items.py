#!/usr/bin/python3

"""
This module provides order_item classes for orders in
Benrays inventory management system
"""

from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, Integer, Float, ForeignKey


class PurchaseOrder(BaseModel, Base):
    """
    Represents purchase orders with product category,
    name, color, quantity, unit_cost_price, total_price,
    order_id, supplier_id, employee_id.
    """
    __tablename__ = "purchase_orders"

    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id"))
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"))
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    unit_cost_price: Mapped[Float] = mapped_column(Float)
    total_price: Mapped[Float] = mapped_column(Float)
    supplier_id: Mapped[str] = mapped_column(ForeignKey("suppliers.id"), nullable=True)
    employee_id: Mapped[str] = mapped_column(ForeignKey("employees.id"))


class CustomerOrder(BaseModel, Base):
    """
    Represents customer orders with product category,
    name, color, quantity, unit_selling_price, total_price,
    order_id, customer_id, employee_id.
    """
    __tablename__ = "customer_orders"

    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id"))
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"))
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    unit_selling_price: Mapped[Float] = mapped_column(Float)
    total_price: Mapped[Float] = mapped_column(Float)
    customer_id: Mapped[str] = mapped_column(ForeignKey("customers.id"), nullable=True)
    employee_id: Mapped[str] = mapped_column(ForeignKey("employees.id"))


class TransferOrder(BaseModel, Base):
    """
    Represents transfer orders for transfering products from one warehouse
    to another with product category, name, color, quantity, unit_cost_price,
    total_price, order_id, supplier_id, employee_id.
    """
    __tablename__ = "transfer_orders"

    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id"))
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"))
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    color_id: Mapped[str] = mapped_column(ForeignKey("colors.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    unit_cost_price: Mapped[Float] = mapped_column(Float)
    total_price: Mapped[Float] = mapped_column(Float)
    transfer_type: Mapped[str] = mapped_column(Enum("IN", "OUT", name="tranfer_type"))
    warehouse_id: Mapped[str] = mapped_column(ForeignKey("warehouses.id"))
    employee_id: Mapped[str] = mapped_column(ForeignKey("employees.id"))
