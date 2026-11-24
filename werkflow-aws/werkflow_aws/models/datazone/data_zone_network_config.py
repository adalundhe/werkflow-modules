from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneNetworkConfig(BaseModel):
    networkAccessType: StrictStr | None = None
    vpcId: StrictStr | None = None
    subnetIds: list[StrictStr] | None = None
    securityGroupIds: list[StrictStr] | None = None
