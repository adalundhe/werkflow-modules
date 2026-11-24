from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsCodeBuildProjectVpcConfig(BaseModel):
    VpcId: StrictStr | None = None
    Subnets: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
