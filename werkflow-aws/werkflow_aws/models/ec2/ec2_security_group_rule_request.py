from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2SecurityGroupRuleRequest(BaseModel):
    IpProtocol: StrictStr | None = None
    FromPort: StrictInt | None = None
    ToPort: StrictInt | None = None
    CidrIpv4: StrictStr | None = None
    CidrIpv6: StrictStr | None = None
    PrefixListId: StrictStr | None = None
    ReferencedGroupId: StrictStr | None = None
    Description: StrictStr | None = None
