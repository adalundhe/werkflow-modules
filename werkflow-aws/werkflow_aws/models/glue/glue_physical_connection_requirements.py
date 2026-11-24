from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GluePhysicalConnectionRequirements(BaseModel):
    SubnetId: StrictStr | None = None
    SecurityGroupIdList: list[StrictStr] | None = None
    AvailabilityZone: StrictStr | None = None
