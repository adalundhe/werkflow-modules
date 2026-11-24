from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_pivoted_label import QuickSightPivotedLabel


class QuickSightPivotConfiguration(BaseModel):
    LabelColumnName: StrictStr | None = None
    PivotedLabels: list[QuickSightPivotedLabel] | None = None
