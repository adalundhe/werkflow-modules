from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetTooltip(BaseModel):
    SheetId: StrictStr | None = None
