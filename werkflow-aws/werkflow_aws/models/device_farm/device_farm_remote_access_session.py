from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .device_farm_device import DeviceFarmDevice
from .device_farm_device_minutes import DeviceFarmDeviceMinutes
from .device_farm_device_proxy import DeviceFarmDeviceProxy
from .device_farm_remote_access_endpoints import DeviceFarmRemoteAccessEndpoints
from .device_farm_vpc_config import DeviceFarmVpcConfig


class DeviceFarmRemoteAccessSession(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    result: StrictStr | None = None
    message: StrictStr | None = None
    started: datetime.datetime | StrictStr | None = None
    stopped: datetime.datetime | StrictStr | None = None
    device: DeviceFarmDevice | None = None
    instanceArn: StrictStr | None = None
    billingMethod: StrictStr | None = None
    deviceMinutes: DeviceFarmDeviceMinutes | None = None
    endpoint: StrictStr | None = None
    deviceUdid: StrictStr | None = None
    interactionMode: StrictStr | None = None
    skipAppResign: StrictBool | None = None
    vpcConfig: DeviceFarmVpcConfig | None = None
    deviceProxy: DeviceFarmDeviceProxy | None = None
    appUpload: StrictStr | None = None
    endpoints: DeviceFarmRemoteAccessEndpoints | None = None
