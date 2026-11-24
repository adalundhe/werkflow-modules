from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceTopology(BaseModel):
    InstanceId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    GroupName: StrictStr | None = None
    NetworkNodes: list[StrictStr] | None = None
    AvailabilityZone: StrictStr | None = None
    ZoneId: StrictStr | None = None
    CapacityBlockId: StrictStr | None = None
