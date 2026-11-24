from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneVpcPropertiesPatch(BaseModel):
    vpcId: StrictStr | None = None
    subnetIds: list[StrictStr] | None = None
    securityGroupId: StrictStr | None = None
