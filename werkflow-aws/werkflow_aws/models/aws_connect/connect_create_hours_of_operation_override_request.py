from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_hours_of_operation_override_config import ConnectHoursOfOperationOverrideConfig
from .connect_recurrence_config import ConnectRecurrenceConfig


class ConnectCreateHoursOfOperationOverrideRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
    Name: StrictStr
    Config: list[ConnectHoursOfOperationOverrideConfig]
    EffectiveFrom: StrictStr
    EffectiveTill: StrictStr
    Description: StrictStr | None = None
    RecurrenceConfig: ConnectRecurrenceConfig | None = None
    OverrideType: Literal['STANDARD', 'OPEN', 'CLOSED'] | None = None
