from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_effective_hours_of_operations import ConnectEffectiveHoursOfOperations
from .connect_effective_override_hours import ConnectEffectiveOverrideHours


class ConnectGetEffectiveHoursOfOperationsResponse(BaseModel):
    EffectiveHoursOfOperationList: list[ConnectEffectiveHoursOfOperations] | None = None
    EffectiveOverrideHoursList: list[ConnectEffectiveOverrideHours] | None = None
    TimeZone: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
