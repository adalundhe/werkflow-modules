from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTVpcDestinationConfiguration(BaseModel):
    subnetIds: list[StrictStr]
    vpcId: StrictStr
    roleArn: StrictStr
    securityGroups: list[StrictStr] | None = None
