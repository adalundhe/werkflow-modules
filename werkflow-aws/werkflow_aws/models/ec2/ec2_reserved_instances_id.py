from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ReservedInstancesId(BaseModel):
    ReservedInstancesId: StrictStr | None = None
