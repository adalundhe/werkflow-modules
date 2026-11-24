from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2ModifyVerifiedAccessEndpointPortRange(BaseModel):
    FromPort: StrictInt | None = None
    ToPort: StrictInt | None = None
