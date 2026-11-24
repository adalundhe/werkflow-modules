from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_drill_down_filter import QuickSightDrillDownFilter


class QuickSightPredefinedHierarchy(BaseModel):
    HierarchyId: StrictStr | None = None
    Columns: list[QuickSightColumnIdentifier] | None = None
    DrillDownFilters: list[QuickSightDrillDownFilter] | None = None
