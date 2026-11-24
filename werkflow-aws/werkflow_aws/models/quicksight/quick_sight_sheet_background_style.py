from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetBackgroundStyle(BaseModel):
    Color: StrictStr | None = None
    Gradient: StrictStr | None = None
