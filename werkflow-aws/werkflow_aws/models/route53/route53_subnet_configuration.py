from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53SubnetConfiguration(BaseModel):
    SubnetId: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    SecurityGroupIdList: list[StrictStr] | None = None
