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

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, sort_order=-3
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        sort_order=-2,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        sort_order=-1,
    )

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
        from models import storage

        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def __str__(self):
        """Returns a user friendly string representation of the object"""
        obj_dict = self.__dict__.copy()
        if "_sa_instance_state" in obj_dict:
            del obj_dict["_sa_instance_state"]
        return f"[{self.__class__.__name__}] ({self.id}) {obj_dict}"

    # def __repr__(self):
    #     """
    #     Return an unambiguous string representation
    #     of the object for debugging and logging.
    #     """
    #     last_item = list(self.__dict__.keys())[-1]
    #     parameters = ""
    #     for attr, value in self.__dict__.items():
    #         if attr == last_item:
    #             parameters = parameters + f"{attr}={value}"
    #         else:
    #             parameters = parameters + f"{attr}={value}" + ", "
    #     return f"{self.__class__.__name__}({parameters})"

    def to_dict(self):
        """Converts objects to dict representation"""
        obj_dict = {}
        obj_dict.update(self.__dict__)
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in obj_dict:
            del obj_dict["_sa_instance_state"]
        return obj_dict
