from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_pivot_table_field_collapse_state_target import QuickSightPivotTableFieldCollapseStateTarget


class QuickSightPivotTableFieldCollapseStateOption(BaseModel):
    Target: QuickSightPivotTableFieldCollapseStateTarget | None = None
    State: StrictStr | None = None
