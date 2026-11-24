from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_pool_cidr_block import EC2PoolCidrBlock
from .ec2_tag_model import EC2TagModel


class EC2Ipv6Pool(BaseModel):
    PoolId: StrictStr | None = None
    Description: StrictStr | None = None
    PoolCidrBlocks: list[EC2PoolCidrBlock] | None = None
    Tags: list[EC2TagModel] | None = None
