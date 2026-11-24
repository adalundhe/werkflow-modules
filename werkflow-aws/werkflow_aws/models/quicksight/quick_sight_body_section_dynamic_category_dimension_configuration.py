from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_column_sort import QuickSightColumnSort


class QuickSightBodySectionDynamicCategoryDimensionConfiguration(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
    Limit: StrictInt | None = None
    SortByMetrics: list[QuickSightColumnSort] | None = None
