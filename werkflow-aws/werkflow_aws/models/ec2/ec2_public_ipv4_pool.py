from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_public_ipv4_pool_range import EC2PublicIpv4PoolRange
from .ec2_tag_model import EC2TagModel


class EC2PublicIpv4Pool(BaseModel):
    PoolId: StrictStr | None = None
    Description: StrictStr | None = None
    PoolAddressRanges: list[EC2PublicIpv4PoolRange] | None = None
    TotalAddressCount: StrictInt | None = None
    TotalAvailableAddressCount: StrictInt | None = None
    NetworkBorderGroup: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
