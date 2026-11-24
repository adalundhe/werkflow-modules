from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneVpcPropertiesOutput(BaseModel):
    vpcId: StrictStr | None = None
    subnetIds: list[StrictStr] | None = None
    status: StrictStr | None = None
    securityGroupId: StrictStr | None = None
    glueConnectionNames: list[StrictStr] | None = None
