from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2CreateVpcLinkRequest(BaseModel):
    Name: StrictStr
    SubnetIds: list[StrictStr]
    SecurityGroupIds: list[StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
