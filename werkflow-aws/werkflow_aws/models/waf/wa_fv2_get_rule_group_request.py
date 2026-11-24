from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2GetRuleGroupRequest(BaseModel):
    Name: StrictStr | None = None
    Scope: Literal['CLOUDFRONT', 'REGIONAL'] | None = None
    Id: StrictStr | None = None
    ARN: StrictStr | None = None
