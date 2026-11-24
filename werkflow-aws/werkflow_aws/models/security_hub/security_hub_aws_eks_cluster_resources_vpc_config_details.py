from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEksClusterResourcesVpcConfigDetails(BaseModel):
    SecurityGroupIds: list[StrictStr] | None = None
    SubnetIds: list[StrictStr] | None = None
    EndpointPublicAccess: StrictBool | None = None
