from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSectionAfterPageBreak(BaseModel):
    Status: StrictStr | None = None
