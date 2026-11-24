from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2ListAvailableManagedRuleGroupVersionsRequest(BaseModel):
    VendorName: StrictStr
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    NextMarker: StrictStr | None = None
    Limit: StrictInt | None = None
