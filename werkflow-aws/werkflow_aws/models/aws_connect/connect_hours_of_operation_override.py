from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_hours_of_operation_override_config import ConnectHoursOfOperationOverrideConfig
from .connect_recurrence_config import ConnectRecurrenceConfig


class ConnectHoursOfOperationOverride(BaseModel):
    HoursOfOperationOverrideId: StrictStr | None = None
    HoursOfOperationId: StrictStr | None = None
    HoursOfOperationArn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Config: list[ConnectHoursOfOperationOverrideConfig] | None = None
    EffectiveFrom: StrictStr | None = None
    EffectiveTill: StrictStr | None = None
    RecurrenceConfig: ConnectRecurrenceConfig | None = None
    OverrideType: StrictStr | None = None
