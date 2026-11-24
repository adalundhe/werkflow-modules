from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildVpcConfig(BaseModel):
    vpcId: StrictStr | None = None
    subnets: list[StrictStr] | None = None
    securityGroupIds: list[StrictStr] | None = None
