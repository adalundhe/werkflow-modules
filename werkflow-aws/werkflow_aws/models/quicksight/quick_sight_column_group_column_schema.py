from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightColumnGroupColumnSchema(BaseModel):
    Name: StrictStr | None = None
