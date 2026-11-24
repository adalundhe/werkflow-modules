from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_user_id_group_pair import EC2UserIdGroupPair


class EC2StaleIpPermission(BaseModel):
    FromPort: StrictInt | None = None
    IpProtocol: StrictStr | None = None
    IpRanges: list[StrictStr] | None = None
    PrefixListIds: list[StrictStr] | None = None
    ToPort: StrictInt | None = None
    UserIdGroupPairs: list[EC2UserIdGroupPair] | None = None
