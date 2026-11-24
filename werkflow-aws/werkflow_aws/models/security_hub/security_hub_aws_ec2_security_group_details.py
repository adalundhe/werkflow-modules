from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ec2_security_group_ip_permission import SecurityHubAwsEc2SecurityGroupIpPermission


class SecurityHubAwsEc2SecurityGroupDetails(BaseModel):
    GroupName: StrictStr | None = None
    GroupId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    VpcId: StrictStr | None = None
    IpPermissions: list[SecurityHubAwsEc2SecurityGroupIpPermission] | None = None
    IpPermissionsEgress: list[SecurityHubAwsEc2SecurityGroupIpPermission] | None = None
