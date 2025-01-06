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
    company_name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(11), nullable=False)
    email: Mapped[str] = mapped_column(String(60), nullable=True)
    city: Mapped[str] = mapped_column(String(20), nullable=False)
    state: Mapped[str] = mapped_column(String(20), nullable=False)
    country: Mapped[str] = mapped_column(String(50), nullable=True)
