from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieGetClassificationScopeRequest(BaseModel):
    id: StrictStr
