from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexSlotValueRegexFilter(BaseModel):
    pattern: StrictStr | None = None
