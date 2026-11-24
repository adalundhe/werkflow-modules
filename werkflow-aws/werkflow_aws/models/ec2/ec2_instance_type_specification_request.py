from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceTypeSpecificationRequest(BaseModel):
    SupportedInstanceTypes: list[StrictStr] | None = None
    UnsupportedInstanceTypes: list[StrictStr] | None = None
