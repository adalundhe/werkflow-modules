from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyTransitGatewayNetworkFunctionAttachmentRequest(BaseModel):
    TransitGatewayAttachmentId: StrictStr
    AddAvailabilityZones: list[StrictStr] | None = None
    AddAvailabilityZoneIds: list[StrictStr] | None = None
    RemoveAvailabilityZones: list[StrictStr] | None = None
    RemoveAvailabilityZoneIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
