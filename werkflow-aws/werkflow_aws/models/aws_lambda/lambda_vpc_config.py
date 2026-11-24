from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LambdaVpcConfig(BaseModel):
    SubnetIds: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    Ipv6AllowedForDualStack: StrictBool | None = None
