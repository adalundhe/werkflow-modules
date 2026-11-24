from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SESPutDedicatedIpPoolScalingAttributesRequest(BaseModel):
    PoolName: StrictStr
    ScalingMode: Literal['STANDARD', 'MANAGED']
