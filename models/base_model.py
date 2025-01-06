#!/usr/bin/python3

"""
This module contains the BaseModel class for
Benrays inventory management system.
"""

from uuid import uuid4
from datetime import datetime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, DateTime

Base = declarative_base()

class BaseModel:
    """
    Defines the base class for all the models
    in Benrays inventory management system.
    """
    id: Mapped[str] =  mapped_column(String, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)


    def __init__(self, **kwargs):
        """
        Initializes attributes for the BaseModel class
        """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            self.__dict__.update(kwargs)

    def save(self):
        """
        Updates timestamp for updated_at attribute and
        saves object to database.
        """
        self.updated_at = datetime.utcnow()
    
    def __repr__(self):
        """
        Return an unambiguous string representation
        of the object for debugging and logging.
        """
        last_item = list(self.__dict__.keys())[-1]
        parameters = ""
        for attr, value in self.__dict__.items():
            if attr == last_item:
                parameters = parameters + f"{attr}={value}"
            else:
                parameters = parameters + f"{attr}={value}" + ", "
        return f"{self.__class__.__name__}({parameters})"

