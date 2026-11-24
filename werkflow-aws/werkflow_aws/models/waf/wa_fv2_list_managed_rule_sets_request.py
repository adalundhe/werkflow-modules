from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2ListManagedRuleSetsRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    NextMarker: StrictStr | None = None
    Limit: StrictInt | None = None
