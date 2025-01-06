#!/usr/bin/python3
"""
This module provides Employee class for
Benrays inventory management system.
"""

from models.base_model import BaseModel, Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float


class Employee(BaseModel, Base):
    """
    Defines the Employees in Benrays inventory management system
    """
    __tablename__ = "employees"

    first_name: Mapped[str] = mapped_column(String(60), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(60), nullable=True)
    last_name: Mapped[str] = mapped_column(String(60), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(11), nullable=False)
    email: Mapped[str] = mapped_column(String(60), nullable=True)
    street: Mapped[str] = mapped_column(String(60), nullable=False)
    city: Mapped[str] = mapped_column(String(60), nullable=False)
    state: Mapped[str] = mapped_column(String(60), nullable=False)
    salary: Mapped[float] = mapped_column(Float, nullable=True)
    role: Mapped[str] = mapped_column(String(20), nullable=False)
    authorization: Mapped[str] = mapped_column(String(200), nullable=True)
    qualification: Mapped[str] = mapped_column(String(60), nullable=False)
