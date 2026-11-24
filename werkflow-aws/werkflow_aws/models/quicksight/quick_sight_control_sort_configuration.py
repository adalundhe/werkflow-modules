from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_aggregation_sort_configuration import QuickSightAggregationSortConfiguration
from .quick_sight_selectable_values_sort import QuickSightSelectableValuesSort


class QuickSightControlSortConfiguration(BaseModel):
    SelectableValuesSort: QuickSightSelectableValuesSort | None = None
    ControlColumnSort: QuickSightAggregationSortConfiguration | None = None
