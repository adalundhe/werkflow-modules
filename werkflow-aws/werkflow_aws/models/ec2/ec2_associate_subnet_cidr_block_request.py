from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2AssociateSubnetCidrBlockRequest(BaseModel):
    SubnetId: StrictStr
    Ipv6IpamPoolId: StrictStr | None = None
    Ipv6NetmaskLength: StrictInt | None = None
    Ipv6CidrBlock: StrictStr | None = None
