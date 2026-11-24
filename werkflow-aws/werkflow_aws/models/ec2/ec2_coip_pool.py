from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2CoipPool(BaseModel):
    PoolId: StrictStr | None = None
    PoolCidrs: list[StrictStr] | None = None
    LocalGatewayRouteTableId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    PoolArn: StrictStr | None = None
