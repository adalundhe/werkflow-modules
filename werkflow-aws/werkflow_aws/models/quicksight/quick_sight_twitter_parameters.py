from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightTwitterParameters(BaseModel):
    Query: StrictStr | None = None
    MaxRows: StrictInt | None = None
