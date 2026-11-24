from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ReservedInstancesConfiguration(BaseModel):
    AvailabilityZone: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    InstanceType: StrictStr | None = None
    Platform: StrictStr | None = None
    Scope: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
