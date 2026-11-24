from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_drill_down_filter import QuickSightDrillDownFilter


class QuickSightDateTimeHierarchy(BaseModel):
    HierarchyId: StrictStr | None = None
    DrillDownFilters: list[QuickSightDrillDownFilter] | None = None
