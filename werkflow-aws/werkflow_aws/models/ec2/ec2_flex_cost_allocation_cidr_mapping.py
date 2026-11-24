from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2FlexCostAllocationCidrMapping(BaseModel):
    CidrRange: StrictStr | None = None
    CidrLabel: StrictStr | None = None
