from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2CarrierGateway(BaseModel):
    CarrierGatewayId: StrictStr | None = None
    VpcId: StrictStr | None = None
    State: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
