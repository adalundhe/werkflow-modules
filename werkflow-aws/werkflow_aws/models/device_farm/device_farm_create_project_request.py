from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .device_farm_environment_variable import DeviceFarmEnvironmentVariable
from .device_farm_vpc_config import DeviceFarmVpcConfig


class DeviceFarmCreateProjectRequest(BaseModel):
    name: StrictStr
    defaultJobTimeoutMinutes: StrictInt | None = None
    vpcConfig: DeviceFarmVpcConfig | None = None
    environmentVariables: list[DeviceFarmEnvironmentVariable] | None = None
    executionRoleArn: StrictStr | None = None
