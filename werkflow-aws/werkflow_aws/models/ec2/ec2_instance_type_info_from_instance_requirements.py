from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceTypeInfoFromInstanceRequirements(BaseModel):
    InstanceType: StrictStr | None = None
