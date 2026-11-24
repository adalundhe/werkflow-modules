from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_dynamic_default_value import QuickSightDynamicDefaultValue
from .quick_sight_rolling_date_configuration import QuickSightRollingDateConfiguration


class QuickSightDateTimeDefaultValues(BaseModel):
    DynamicValue: QuickSightDynamicDefaultValue | None = None
    StaticValues: list[datetime.datetime | StrictStr] | None = None
    RollingDate: QuickSightRollingDateConfiguration | None = None
