from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightVisualHighlightOperation(BaseModel):
    Trigger: StrictStr | None = None
