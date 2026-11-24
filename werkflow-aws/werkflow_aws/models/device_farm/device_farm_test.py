from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .device_farm_counters import DeviceFarmCounters
from .device_farm_device_minutes import DeviceFarmDeviceMinutes


class DeviceFarmTest(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    result: StrictStr | None = None
    started: datetime.datetime | StrictStr | None = None
    stopped: datetime.datetime | StrictStr | None = None
    counters: DeviceFarmCounters | None = None
    message: StrictStr | None = None
    deviceMinutes: DeviceFarmDeviceMinutes | None = None
