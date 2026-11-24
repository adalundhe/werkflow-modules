from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFDeprecateDomainRequest(BaseModel):
    name: StrictStr
