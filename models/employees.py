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

    first_name: Mapped[str] = mapped_column(String(30))
    middle_name: Mapped[str] = mapped_column(String(30), nullable=True)
    last_name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(Enum("male", "female"))
    marital_status: Mapped[str] = mapped_column(Enum("single", "married"))
    phone_number: Mapped[str] = mapped_column(String(11))
    email: Mapped[str] = mapped_column(String(60), unique=True)
    password: Mapped[str] = mapped_column(String(60))
    street: Mapped[str] = mapped_column(String(60))
    city: Mapped[str] = mapped_column(String(60))
    state: Mapped[str] = mapped_column(String(20))
    role: Mapped[str] = mapped_column(String(30))
    work_experience: Mapped[str] = mapped_column(String(200), nullable=True)
    qualifications: Mapped[str] = mapped_column(String(150), nullable=True)
    name_of_guarantor: Mapped[str] = mapped_column(String(150))
    guarantor_contact: Mapped[str] = mapped_column(String(11))
    salary: Mapped[float] = mapped_column(Float, default=0.00)
    permissions: Mapped[str] = mapped_column(String(200), nullable=True)

    warehouses: Mapped[list["Warehouse"]] = relationship(
                                                secondary=warehouse_employee,
                                                back_populates="employees",
                                            )
