from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_stale_ip_permission import EC2StaleIpPermission


class EC2StaleSecurityGroup(BaseModel):
    Description: StrictStr | None = None
    GroupId: StrictStr | None = None
    GroupName: StrictStr | None = None
    StaleIpPermissions: list[EC2StaleIpPermission] | None = None
    StaleIpPermissionsEgress: list[EC2StaleIpPermission] | None = None
    VpcId: StrictStr | None = None
