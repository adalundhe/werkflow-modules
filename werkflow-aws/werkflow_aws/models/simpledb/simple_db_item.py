from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .simple_db_attribute import SimpleDBAttribute


class SimpleDBItem(BaseModel):
    Name: StrictStr | None = None
    AlternateNameEncoding: StrictStr | None = None
    Attributes: list[SimpleDBAttribute] | None = None
