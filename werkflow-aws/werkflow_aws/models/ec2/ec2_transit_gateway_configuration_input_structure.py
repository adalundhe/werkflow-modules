from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayConfigurationInputStructure(BaseModel):
    TransitGatewayId: StrictStr | None = None
    AvailabilityZones: list[StrictStr] | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
