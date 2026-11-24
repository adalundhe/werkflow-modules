from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_referenced_security_group import EC2ReferencedSecurityGroup
from .ec2_tag_model import EC2TagModel


class EC2SecurityGroupRule(BaseModel):
    SecurityGroupRuleId: StrictStr | None = None
    GroupId: StrictStr | None = None
    GroupOwnerId: StrictStr | None = None
    IsEgress: StrictBool | None = None
    IpProtocol: StrictStr | None = None
    FromPort: StrictInt | None = None
    ToPort: StrictInt | None = None
    CidrIpv4: StrictStr | None = None
    CidrIpv6: StrictStr | None = None
    PrefixListId: StrictStr | None = None
    ReferencedGroupInfo: EC2ReferencedSecurityGroup | None = None
    Description: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    SecurityGroupRuleArn: StrictStr | None = None
