from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneVpcPropertiesInput(BaseModel):
    vpcId: StrictStr
    subnetIds: list[StrictStr]
    securityGroupId: StrictStr | None = None
