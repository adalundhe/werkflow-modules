from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2AssociateVpcCidrBlockRequest(BaseModel):
    VpcId: StrictStr
    CidrBlock: StrictStr | None = None
    Ipv6CidrBlockNetworkBorderGroup: StrictStr | None = None
    Ipv6Pool: StrictStr | None = None
    Ipv6CidrBlock: StrictStr | None = None
    Ipv4IpamPoolId: StrictStr | None = None
    Ipv4NetmaskLength: StrictInt | None = None
    Ipv6IpamPoolId: StrictStr | None = None
    Ipv6NetmaskLength: StrictInt | None = None
    AmazonProvidedIpv6CidrBlock: StrictBool | None = None
