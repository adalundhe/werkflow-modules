from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .simple_db_attribute import SimpleDBAttribute


class SimpleDBDeletableItem(BaseModel):
    Name: StrictStr
    Attributes: list[SimpleDBAttribute] | None = None
