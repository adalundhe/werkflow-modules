from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .storage_gateway_software_update_preferences import StorageGatewaySoftwareUpdatePreferences


class StorageGatewayDescribeMaintenanceStartTimeResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    HourOfDay: StrictInt | None = None
    MinuteOfHour: StrictInt | None = None
    DayOfWeek: StrictInt | None = None
    DayOfMonth: StrictInt | None = None
    Timezone: StrictStr | None = None
    SoftwareUpdatePreferences: StorageGatewaySoftwareUpdatePreferences | None = None
    ResponseMetadata: dict[str, Any] | None = None
