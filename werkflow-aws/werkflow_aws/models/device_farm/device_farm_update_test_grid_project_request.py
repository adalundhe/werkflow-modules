from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_test_grid_vpc_config import DeviceFarmTestGridVpcConfig


class DeviceFarmUpdateTestGridProjectRequest(BaseModel):
    projectArn: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    vpcConfig: DeviceFarmTestGridVpcConfig | None = None
