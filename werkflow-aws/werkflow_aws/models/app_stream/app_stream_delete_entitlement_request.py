from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDeleteEntitlementRequest(BaseModel):
    Name: StrictStr
    StackName: StrictStr
