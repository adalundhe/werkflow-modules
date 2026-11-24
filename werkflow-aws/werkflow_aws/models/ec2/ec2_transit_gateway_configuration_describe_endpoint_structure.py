from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayConfigurationDescribeEndpointStructure(BaseModel):
    TransitGatewayId: StrictStr | None = None
    TransitGatewayAttachmentId: StrictStr | None = None
    AvailabilityZones: list[StrictStr] | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
