from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2ExcludedRule(BaseModel):
    Name: StrictStr | None = None
