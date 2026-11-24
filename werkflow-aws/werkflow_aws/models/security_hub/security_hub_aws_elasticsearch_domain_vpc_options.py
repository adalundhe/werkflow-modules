from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsElasticsearchDomainVPCOptions(BaseModel):
    AvailabilityZones: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SubnetIds: list[StrictStr] | None = None
    VPCId: StrictStr | None = None
