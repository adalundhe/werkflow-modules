from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2DeleteRuleGroupRequest(BaseModel):
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Id: StrictStr
    LockToken: StrictStr
