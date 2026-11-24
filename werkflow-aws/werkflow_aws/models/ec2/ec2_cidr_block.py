from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CidrBlock(BaseModel):
    CidrBlock: StrictStr | None = None
