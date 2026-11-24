from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetCapacityProviderRequest(BaseModel):
    CapacityProviderName: StrictStr
