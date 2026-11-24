from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetImageTooltipText(BaseModel):
    PlainText: StrictStr | None = None
