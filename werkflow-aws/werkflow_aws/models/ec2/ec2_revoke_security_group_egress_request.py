from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_ip_permission import EC2IpPermission


class EC2RevokeSecurityGroupEgressRequest(BaseModel):
    GroupId: StrictStr
    SecurityGroupRuleIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
    SourceSecurityGroupName: StrictStr | None = None
    SourceSecurityGroupOwnerId: StrictStr | None = None
    IpProtocol: StrictStr | None = None
    FromPort: StrictInt | None = None
    ToPort: StrictInt | None = None
    CidrIp: StrictStr | None = None
    IpPermissions: list[EC2IpPermission] | None = None
