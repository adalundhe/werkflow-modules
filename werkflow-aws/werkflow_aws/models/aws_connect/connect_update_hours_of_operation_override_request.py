from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_hours_of_operation_override_config import ConnectHoursOfOperationOverrideConfig
from .connect_recurrence_config import ConnectRecurrenceConfig


class ConnectUpdateHoursOfOperationOverrideRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
    HoursOfOperationOverrideId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Config: list[ConnectHoursOfOperationOverrideConfig] | None = None
    EffectiveFrom: StrictStr | None = None
    EffectiveTill: StrictStr | None = None
    RecurrenceConfig: ConnectRecurrenceConfig | None = None
    OverrideType: Literal['STANDARD', 'OPEN', 'CLOSED'] | None = None
