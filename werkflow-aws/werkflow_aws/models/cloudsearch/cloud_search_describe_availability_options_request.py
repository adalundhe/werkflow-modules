from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchDescribeAvailabilityOptionsRequest(BaseModel):
    DomainName: StrictStr
    Deployed: StrictBool | None = None
