from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTVpcDestinationProperties(BaseModel):
    subnetIds: list[StrictStr] | None = None
    securityGroups: list[StrictStr] | None = None
    vpcId: StrictStr | None = None
    roleArn: StrictStr | None = None
