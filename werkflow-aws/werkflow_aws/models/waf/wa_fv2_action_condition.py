from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2ActionCondition(BaseModel):
    Action: StrictStr | None = None
