from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2FlexCostAllocationNetworkResourceScope(BaseModel):
    ResourceType: Literal['account', 'vpc', 'subnet']
    ResourceIds: list[StrictStr]
