from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2TransitGatewayPolicyTable(BaseModel):
    TransitGatewayPolicyTableId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    State: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
