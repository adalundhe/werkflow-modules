from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_custom_filter_configuration import QuickSightCustomFilterConfiguration
from .quick_sight_custom_filter_list_configuration import QuickSightCustomFilterListConfiguration
from .quick_sight_filter_list_configuration import QuickSightFilterListConfiguration


class QuickSightCategoryFilterConfiguration(BaseModel):
    FilterListConfiguration: QuickSightFilterListConfiguration | None = None
    CustomFilterListConfiguration: QuickSightCustomFilterListConfiguration | None = None
    CustomFilterConfiguration: QuickSightCustomFilterConfiguration | None = None
