from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .simple_db_attribute import SimpleDBAttribute


class SimpleDBGetAttributesResponse(BaseModel):
    Attributes: list[SimpleDBAttribute] | None = None
    ResponseMetadata: dict[str, Any] | None = None
