from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceTypeOffering(BaseModel):
    InstanceType: StrictStr | None = None
    LocationType: StrictStr | None = None
    Location: StrictStr | None = None
