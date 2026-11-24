from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_instance_profile import DeviceFarmInstanceProfile


class DeviceFarmDeviceInstance(BaseModel):
    arn: StrictStr | None = None
    deviceArn: StrictStr | None = None
    labels: list[StrictStr] | None = None
    status: StrictStr | None = None
    udid: StrictStr | None = None
    instanceProfile: DeviceFarmInstanceProfile | None = None
