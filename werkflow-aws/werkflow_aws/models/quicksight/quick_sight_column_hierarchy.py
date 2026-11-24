from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_date_time_hierarchy import QuickSightDateTimeHierarchy
from .quick_sight_explicit_hierarchy import QuickSightExplicitHierarchy
from .quick_sight_predefined_hierarchy import QuickSightPredefinedHierarchy


class QuickSightColumnHierarchy(BaseModel):
    ExplicitHierarchy: QuickSightExplicitHierarchy | None = None
    DateTimeHierarchy: QuickSightDateTimeHierarchy | None = None
    PredefinedHierarchy: QuickSightPredefinedHierarchy | None = None
