from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightColumnDescription(BaseModel):
    Text: StrictStr | None = None
