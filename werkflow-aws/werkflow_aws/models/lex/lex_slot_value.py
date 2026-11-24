from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexSlotValue(BaseModel):
    interpretedValue: StrictStr | None = None
