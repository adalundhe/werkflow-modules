from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRdsDbSecurityGroupEc2SecurityGroup(BaseModel):
    Ec2SecurityGroupId: StrictStr | None = None
    Ec2SecurityGroupName: StrictStr | None = None
    Ec2SecurityGroupOwnerId: StrictStr | None = None
    Status: StrictStr | None = None
