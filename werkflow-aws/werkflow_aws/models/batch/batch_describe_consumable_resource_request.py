from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchDescribeConsumableResourceRequest(BaseModel):
    consumableResource: StrictStr
