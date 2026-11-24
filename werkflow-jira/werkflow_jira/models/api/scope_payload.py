from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ScopePayload(BaseModel):
    type: StrictStr | None = None
