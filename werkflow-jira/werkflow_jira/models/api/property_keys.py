from __future__ import annotations
from pydantic import BaseModel
from .property_key import PropertyKey


class PropertyKeys(BaseModel):
    keys: list[PropertyKey] | None = None
