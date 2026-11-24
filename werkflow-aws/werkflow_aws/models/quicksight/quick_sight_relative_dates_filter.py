from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_anchor_date_configuration import QuickSightAnchorDateConfiguration
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_default_filter_control_configuration import QuickSightDefaultFilterControlConfiguration
from .quick_sight_exclude_period_configuration import QuickSightExcludePeriodConfiguration


class QuickSightRelativeDatesFilter(BaseModel):
    FilterId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    AnchorDateConfiguration: QuickSightAnchorDateConfiguration | None = None
    MinimumGranularity: StrictStr | None = None
    TimeGranularity: StrictStr | None = None
    RelativeDateType: StrictStr | None = None
    RelativeDateValue: StrictInt | None = None
    ParameterName: StrictStr | None = None
    NullOption: StrictStr | None = None
    ExcludePeriodConfiguration: QuickSightExcludePeriodConfiguration | None = None
    DefaultFilterControlConfiguration: QuickSightDefaultFilterControlConfiguration | None = None
