from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2TransitGatewayNetworkFunctionAttachment(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    TransitGatewayOwnerId: StrictStr | None = None
    ResourceOwnerId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    AvailabilityZones: list[StrictStr] | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
    State: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
