from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_aggregation_sort_configuration import QuickSightAggregationSortConfiguration
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_default_filter_control_configuration import QuickSightDefaultFilterControlConfiguration


class QuickSightTopBottomFilter(BaseModel):
    FilterId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    Limit: StrictInt | None = None
    AggregationSortConfigurations: list[QuickSightAggregationSortConfiguration] | None = None
    TimeGranularity: StrictStr | None = None
    ParameterName: StrictStr | None = None
    DefaultFilterControlConfiguration: QuickSightDefaultFilterControlConfiguration | None = None
