from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PoolCidrBlock(BaseModel):
    Cidr: StrictStr | None = None
