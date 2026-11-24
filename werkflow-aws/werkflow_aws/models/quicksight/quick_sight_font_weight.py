from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFontWeight(BaseModel):
    Name: StrictStr | None = None
