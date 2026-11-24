from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_internet_gateway_attachment import EC2InternetGatewayAttachment
from .ec2_tag_model import EC2TagModel


class EC2InternetGateway(BaseModel):
    Attachments: list[EC2InternetGatewayAttachment] | None = None
    InternetGatewayId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
