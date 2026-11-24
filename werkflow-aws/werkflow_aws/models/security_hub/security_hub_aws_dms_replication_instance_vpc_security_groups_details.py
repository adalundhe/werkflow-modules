from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsDmsReplicationInstanceVpcSecurityGroupsDetails(BaseModel):
    VpcSecurityGroupId: StrictStr | None = None
