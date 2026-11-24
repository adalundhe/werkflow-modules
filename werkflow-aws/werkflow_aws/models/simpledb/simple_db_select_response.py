from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .simple_db_item import SimpleDBItem


class SimpleDBSelectResponse(BaseModel):
    Items: list[SimpleDBItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
