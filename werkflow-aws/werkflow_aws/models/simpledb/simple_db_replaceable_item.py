from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .simple_db_replaceable_attribute import SimpleDBReplaceableAttribute


class SimpleDBReplaceableItem(BaseModel):
    Name: StrictStr
    Attributes: list[SimpleDBReplaceableAttribute]
