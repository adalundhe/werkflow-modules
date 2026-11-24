from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataSetStringFilterValue(BaseModel):
    StaticValue: StrictStr | None = None
