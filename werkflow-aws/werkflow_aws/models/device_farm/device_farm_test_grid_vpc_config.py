from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmTestGridVpcConfig(BaseModel):
    securityGroupIds: list[StrictStr] | None = None
    subnetIds: list[StrictStr] | None = None
    vpcId: StrictStr | None = None
