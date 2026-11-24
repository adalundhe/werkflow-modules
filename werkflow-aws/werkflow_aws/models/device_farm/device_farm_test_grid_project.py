from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .device_farm_test_grid_vpc_config import DeviceFarmTestGridVpcConfig


class DeviceFarmTestGridProject(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    vpcConfig: DeviceFarmTestGridVpcConfig | None = None
    created: datetime.datetime | StrictStr | None = None
