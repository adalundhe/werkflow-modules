from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CapacityReservationTopology(BaseModel):
    CapacityReservationId: StrictStr | None = None
    CapacityBlockId: StrictStr | None = None
    State: StrictStr | None = None
    InstanceType: StrictStr | None = None
    GroupName: StrictStr | None = None
    NetworkNodes: list[StrictStr] | None = None
    AvailabilityZoneId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
