from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_default_filter_control_configuration import QuickSightDefaultFilterControlConfiguration
from .quick_sight_rolling_date_configuration import QuickSightRollingDateConfiguration


class QuickSightTimeEqualityFilter(BaseModel):
    FilterId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    Value: datetime.datetime | StrictStr | None = None
    ParameterName: StrictStr | None = None
    TimeGranularity: StrictStr | None = None
    RollingDate: QuickSightRollingDateConfiguration | None = None
    DefaultFilterControlConfiguration: QuickSightDefaultFilterControlConfiguration | None = None
