from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightCategoryDrillDownFilter(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
    CategoryValues: list[StrictStr] | None = None
