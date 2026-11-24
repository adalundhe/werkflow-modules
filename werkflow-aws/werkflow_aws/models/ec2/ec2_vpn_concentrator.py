from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2VpnConcentrator(BaseModel):
    VpnConcentratorId: StrictStr | None = None
    State: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    TransitGatewayAttachmentId: StrictStr | None = None
    Type: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
