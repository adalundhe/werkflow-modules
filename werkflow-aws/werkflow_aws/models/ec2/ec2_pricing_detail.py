from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class EC2PricingDetail(BaseModel):
    Count: StrictInt | None = None
    Price: StrictFloat | StrictInt | None = None
