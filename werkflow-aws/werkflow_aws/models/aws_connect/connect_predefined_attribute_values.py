from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPredefinedAttributeValues(BaseModel):
    StringList: list[StrictStr] | None = None
