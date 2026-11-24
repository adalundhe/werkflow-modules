from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFUndeprecateDomainRequest(BaseModel):
    name: StrictStr
