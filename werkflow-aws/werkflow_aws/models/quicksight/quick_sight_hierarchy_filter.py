from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_default_filter_control_configuration import QuickSightDefaultFilterControlConfiguration
from .quick_sight_hierarchy_filter_level import QuickSightHierarchyFilterLevel
from .quick_sight_hierarchy_filter_node import QuickSightHierarchyFilterNode


class QuickSightHierarchyFilter(BaseModel):
    FilterId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    HierarchyLevels: list[QuickSightHierarchyFilterLevel] | None = None
    HierarchyTree: QuickSightHierarchyFilterNode | None = None
    NullOption: StrictStr | None = None
    MatchOperator: StrictStr | None = None
    DefaultFilterControlConfiguration: QuickSightDefaultFilterControlConfiguration | None = None
