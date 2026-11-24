from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFont(BaseModel):
    FontFamily: StrictStr | None = None
