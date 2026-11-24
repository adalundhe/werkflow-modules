from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_category_filter_configuration import QuickSightCategoryFilterConfiguration
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_default_filter_control_configuration import QuickSightDefaultFilterControlConfiguration


class QuickSightCategoryFilter(BaseModel):
    FilterId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    Configuration: QuickSightCategoryFilterConfiguration | None = None
    DefaultFilterControlConfiguration: QuickSightDefaultFilterControlConfiguration | None = None
