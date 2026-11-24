from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .device_farm_cpu import DeviceFarmCPU
from .device_farm_device_instance import DeviceFarmDeviceInstance
from .device_farm_resolution import DeviceFarmResolution


class DeviceFarmDevice(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    manufacturer: StrictStr | None = None
    model: StrictStr | None = None
    modelId: StrictStr | None = None
    formFactor: StrictStr | None = None
    platform: StrictStr | None = None
    type: StrictStr | None = None
    os: StrictStr | None = None
    cpu: DeviceFarmCPU | None = None
    resolution: DeviceFarmResolution | None = None
    heapSize: StrictInt | None = None
    memory: StrictInt | None = None
    image: StrictStr | None = None
    carrier: StrictStr | None = None
    radio: StrictStr | None = None
    remoteAccessEnabled: StrictBool | None = None
    remoteDebugEnabled: StrictBool | None = None
    fleetType: StrictStr | None = None
    fleetName: StrictStr | None = None
    instances: list[DeviceFarmDeviceInstance] | None = None
    availability: StrictStr | None = None
