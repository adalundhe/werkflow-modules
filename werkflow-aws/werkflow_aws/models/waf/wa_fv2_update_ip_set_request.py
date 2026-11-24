from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2UpdateIPSetRequest(BaseModel):
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Id: StrictStr
    Addresses: list[StrictStr]
    LockToken: StrictStr
    Description: StrictStr | None = None
