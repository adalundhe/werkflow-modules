from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_aggregation_function import QuickSightAggregationFunction
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_default_filter_control_configuration import QuickSightDefaultFilterControlConfiguration
from .quick_sight_numeric_range_filter_value import QuickSightNumericRangeFilterValue


class QuickSightNumericRangeFilter(BaseModel):
    FilterId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    IncludeMinimum: StrictBool | None = None
    IncludeMaximum: StrictBool | None = None
    RangeMinimum: QuickSightNumericRangeFilterValue | None = None
    RangeMaximum: QuickSightNumericRangeFilterValue | None = None
    SelectAllOptions: StrictStr | None = None
    AggregationFunction: QuickSightAggregationFunction | None = None
    NullOption: StrictStr | None = None
    DefaultFilterControlConfiguration: QuickSightDefaultFilterControlConfiguration | None = None
