from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_ip_range import EC2IpRange
from .ec2_ipv6_range import EC2Ipv6Range
from .ec2_prefix_list_id import EC2PrefixListId
from .ec2_user_id_group_pair import EC2UserIdGroupPair


class EC2IpPermission(BaseModel):
    IpProtocol: StrictStr | None = None
    FromPort: StrictInt | None = None
    ToPort: StrictInt | None = None
    UserIdGroupPairs: list[EC2UserIdGroupPair] | None = None
    IpRanges: list[EC2IpRange] | None = None
    Ipv6Ranges: list[EC2Ipv6Range] | None = None
    PrefixListIds: list[EC2PrefixListId] | None = None
