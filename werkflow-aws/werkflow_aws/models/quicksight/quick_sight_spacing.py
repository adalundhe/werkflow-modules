from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSpacing(BaseModel):
    Top: StrictStr | None = None
    Bottom: StrictStr | None = None
    Left: StrictStr | None = None
    Right: StrictStr | None = None
