from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2TransitGatewayMeteringPolicy(BaseModel):
    TransitGatewayMeteringPolicyId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    MiddleboxAttachmentIds: list[StrictStr] | None = None
    State: StrictStr | None = None
    UpdateEffectiveAt: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
