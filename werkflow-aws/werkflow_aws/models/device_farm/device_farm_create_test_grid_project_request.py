from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_test_grid_vpc_config import DeviceFarmTestGridVpcConfig


class DeviceFarmCreateTestGridProjectRequest(BaseModel):
    name: StrictStr
    description: StrictStr | None = None
    vpcConfig: DeviceFarmTestGridVpcConfig | None = None
