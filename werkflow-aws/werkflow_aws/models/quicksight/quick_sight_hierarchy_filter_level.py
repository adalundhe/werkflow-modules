from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightHierarchyFilterLevel(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
