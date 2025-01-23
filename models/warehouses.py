#!/usr/bin/python3

"""
This module provides Warehouse class for
Benrays inventory management system.
"""


from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Table, Column, ForeignKey


warehouse_product = Table(
    "warehouse_products",
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("Warehouse_id", ForeignKey("warehouses.id"), primary_key=True)
)

warehouse_employee = Table(
    "warehouse_employees",
    Base.metadata,
    Column("warehouse_id", ForeignKey("warehouses.id"), primary_key=True),
    Column("Employee_id", ForeignKey("employees.id"), primary_key=True)
)

class Warehouse(BaseModel, Base):
    """
    Defines the Warehouses in Benrays inventory management system
    """
    __tablename__ = "warehouses"
    name: Mapped[str] = mapped_column(String(60), unique=True)
    phone_number: Mapped[str] = mapped_column(String(11))
    street: Mapped[str] = mapped_column(String(60))
    city: Mapped[str] = mapped_column(String(20))
    state: Mapped[str] = mapped_column(String(20))

    products: Mapped[list["Product"]] = relationship(
                                            secondary= warehouse_product,
                                            backref="warehouses",
                                        )
    employees: Mapped[list["Employee"]] = relationship(
                                            secondary= warehouse_employee,
                                            back_populates="warehouses",
                                        )
