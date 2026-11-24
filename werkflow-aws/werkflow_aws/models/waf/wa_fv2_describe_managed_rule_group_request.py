from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2DescribeManagedRuleGroupRequest(BaseModel):
    VendorName: StrictStr
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    VersionName: StrictStr | None = None
