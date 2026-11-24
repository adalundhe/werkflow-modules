from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .storage_gateway_software_update_preferences import StorageGatewaySoftwareUpdatePreferences


class StorageGatewayUpdateMaintenanceStartTimeRequest(BaseModel):
    GatewayARN: StrictStr
    HourOfDay: StrictInt | None = None
    MinuteOfHour: StrictInt | None = None
    DayOfWeek: StrictInt | None = None
    DayOfMonth: StrictInt | None = None
    SoftwareUpdatePreferences: StorageGatewaySoftwareUpdatePreferences | None = None
