from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53GetReusableDelegationSetLimitRequest(BaseModel):
    Type: Literal['MAX_ZONES_BY_REUSABLE_DELEGATION_SET']
    DelegationSetId: StrictStr
