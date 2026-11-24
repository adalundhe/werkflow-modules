from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRedshiftClusterVpcSecurityGroup(BaseModel):
    Status: StrictStr | None = None
    VpcSecurityGroupId: StrictStr | None = None
