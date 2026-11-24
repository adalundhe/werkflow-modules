from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails(BaseModel):
    AssignPublicIp: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
    Subnets: list[StrictStr] | None = None
