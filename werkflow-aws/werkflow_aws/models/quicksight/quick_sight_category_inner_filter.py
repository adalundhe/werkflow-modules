from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_category_filter_configuration import QuickSightCategoryFilterConfiguration
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_default_filter_control_configuration import QuickSightDefaultFilterControlConfiguration


class QuickSightCategoryInnerFilter(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
    Configuration: QuickSightCategoryFilterConfiguration | None = None
    DefaultFilterControlConfiguration: QuickSightDefaultFilterControlConfiguration | None = None
