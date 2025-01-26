#!/usr/bin/python3
"""
This module provides Employee class for
Benrays inventory management system.
"""

from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Supplier(BaseModel, Base):
    """
    Defines the Warehouses in Benrays inventory management system
    """

    __tablename__ = "suppliers"
    company_name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(11))
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    street: Mapped[str] = mapped_column(String(60), nullable=True)
    city: Mapped[str] = mapped_column(String(60))
    state: Mapped[str] = mapped_column(String(60))
    country: Mapped[str] = mapped_column(String(60), default="Nigeria")
