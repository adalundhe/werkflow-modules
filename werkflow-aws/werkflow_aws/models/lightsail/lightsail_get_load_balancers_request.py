from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetLoadBalancersRequest(BaseModel):
    pageToken: StrictStr | None = None
