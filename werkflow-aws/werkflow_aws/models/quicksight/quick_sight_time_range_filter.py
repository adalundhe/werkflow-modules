from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_default_filter_control_configuration import QuickSightDefaultFilterControlConfiguration
from .quick_sight_exclude_period_configuration import QuickSightExcludePeriodConfiguration
from .quick_sight_time_range_filter_value import QuickSightTimeRangeFilterValue


class QuickSightTimeRangeFilter(BaseModel):
    FilterId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    IncludeMinimum: StrictBool | None = None
    IncludeMaximum: StrictBool | None = None
    RangeMinimumValue: QuickSightTimeRangeFilterValue | None = None
    RangeMaximumValue: QuickSightTimeRangeFilterValue | None = None
    NullOption: StrictStr | None = None
    ExcludePeriodConfiguration: QuickSightExcludePeriodConfiguration | None = None
    TimeGranularity: StrictStr | None = None
    DefaultFilterControlConfiguration: QuickSightDefaultFilterControlConfiguration | None = None
