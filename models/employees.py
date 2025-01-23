#!/usr/bin/python3
"""
This module provides Employee class for
Benrays inventory management system.
"""

from models.base_model import BaseModel, Base
from models.warehouses import warehouse_employee

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, Enum


class Employee(BaseModel, Base):
    """
    Defines the Employees in Benrays inventory management system
    """
    __tablename__ = "employees"

    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    gender: Mapped[str] = mapped_column(Enum("male", "female"), nullable=False)
    marital_status: Mapped[str] = mapped_column(Enum("single", "married"), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(11), nullable=False)
    email: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    street: Mapped[str] = mapped_column(String(60), nullable=False)
    city: Mapped[str] = mapped_column(String(60), nullable=False)
    state: Mapped[str] = mapped_column(String(20), nullable=False)
    role: Mapped[str] = mapped_column(String(30), nullable=False)
    work_experience: Mapped[str] = mapped_column(String(200))
    qualifications: Mapped[str] = mapped_column(String(150))
    name_of_guarantor: Mapped[str] = mapped_column(String(150), nullable=False)
    guarantor_contact: Mapped[str] = mapped_column(String(11), nullable=False)
    salary: Mapped[float] = mapped_column(Float, default=0.00)
    permissions: Mapped[str] = mapped_column(String(200))

    warehouses: Mapped[list["Warehouse"]] = relationship(
                                                secondary=warehouse_employee,
                                                back_populates="employees",
                                            )
