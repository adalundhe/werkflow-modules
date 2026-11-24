from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .device_farm_counters import DeviceFarmCounters
from .device_farm_device import DeviceFarmDevice
from .device_farm_device_minutes import DeviceFarmDeviceMinutes
from .device_farm_job_insights import DeviceFarmJobInsights


class DeviceFarmJob(BaseModel):
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
    device: DeviceFarmDevice | None = None
    instanceArn: StrictStr | None = None
    deviceMinutes: DeviceFarmDeviceMinutes | None = None
    videoEndpoint: StrictStr | None = None
    videoCapture: StrictBool | None = None
    insights: DeviceFarmJobInsights | None = None
