from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_ip_permission import EC2IpPermission
from .ec2_security_group_rule_description import EC2SecurityGroupRuleDescription


class EC2UpdateSecurityGroupRuleDescriptionsIngressRequest(BaseModel):
    DryRun: StrictBool | None = None
    GroupId: StrictStr | None = None
    GroupName: StrictStr | None = None
    IpPermissions: list[EC2IpPermission] | None = None
    SecurityGroupRuleDescriptions: list[EC2SecurityGroupRuleDescription] | None = None
