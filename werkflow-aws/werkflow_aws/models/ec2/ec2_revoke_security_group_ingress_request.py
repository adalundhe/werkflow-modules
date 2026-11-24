from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_ip_permission import EC2IpPermission


class EC2RevokeSecurityGroupIngressRequest(BaseModel):
    CidrIp: StrictStr | None = None
    FromPort: StrictInt | None = None
    GroupId: StrictStr | None = None
    GroupName: StrictStr | None = None
    IpPermissions: list[EC2IpPermission] | None = None
    IpProtocol: StrictStr | None = None
    SourceSecurityGroupName: StrictStr | None = None
    SourceSecurityGroupOwnerId: StrictStr | None = None
    ToPort: StrictInt | None = None
    SecurityGroupRuleIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
