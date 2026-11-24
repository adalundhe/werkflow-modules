from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53CidrBlockSummary(BaseModel):
    CidrBlock: StrictStr | None = None
    LocationName: StrictStr | None = None
