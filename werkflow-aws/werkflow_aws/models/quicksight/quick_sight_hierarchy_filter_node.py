from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightHierarchyFilterNode(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
    ParentValue: StrictStr | None = None
    HierarchyValues: list[StrictStr] | None = None
    Children: list[QuickSightHierarchyFilterNode] | None = None
