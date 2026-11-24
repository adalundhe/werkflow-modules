from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_ec2_security_group_ip_range import SecurityHubAwsEc2SecurityGroupIpRange
from .security_hub_aws_ec2_security_group_ipv6_range import SecurityHubAwsEc2SecurityGroupIpv6Range
from .security_hub_aws_ec2_security_group_prefix_list_id import SecurityHubAwsEc2SecurityGroupPrefixListId
from .security_hub_aws_ec2_security_group_user_id_group_pair import SecurityHubAwsEc2SecurityGroupUserIdGroupPair


class SecurityHubAwsEc2SecurityGroupIpPermission(BaseModel):
    IpProtocol: StrictStr | None = None
    FromPort: StrictInt | None = None
    ToPort: StrictInt | None = None
    UserIdGroupPairs: list[SecurityHubAwsEc2SecurityGroupUserIdGroupPair] | None = None
    IpRanges: list[SecurityHubAwsEc2SecurityGroupIpRange] | None = None
    Ipv6Ranges: list[SecurityHubAwsEc2SecurityGroupIpv6Range] | None = None
    PrefixListIds: list[SecurityHubAwsEc2SecurityGroupPrefixListId] | None = None
