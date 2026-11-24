from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSameSheetTargetVisualConfiguration(BaseModel):
    TargetVisuals: list[StrictStr] | None = None
    TargetVisualOptions: StrictStr | None = None
