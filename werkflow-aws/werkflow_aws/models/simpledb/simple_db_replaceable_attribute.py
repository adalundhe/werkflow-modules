from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SimpleDBReplaceableAttribute(BaseModel):
    Name: StrictStr
    Value: StrictStr
    Replace: StrictBool | None = None
