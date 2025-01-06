#!/usr/bin/python3

"""
This module provides Warehouse class for
Benrays inventory management system.
"""


from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Warehouse(BaseModel, Base):
    """
    Defines the Warehouses in Benrays inventory management system
    """
    __tablename__ = "warehouses"
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(11), nullable=False)
    street: Mapped[str] = mapped_column(String(60), nullable=False)
    city: Mapped[str] = mapped_column(String(20), nullable=False)
    state: Mapped[str] = mapped_column(String(20), nullable=False)
