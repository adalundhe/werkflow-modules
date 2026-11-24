from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCreateVpcEndpointRequest(BaseModel):
    name: StrictStr
    vpcId: StrictStr
    subnetIds: list[StrictStr]
    securityGroupIds: list[StrictStr] | None = None
    clientToken: StrictStr | None = None
