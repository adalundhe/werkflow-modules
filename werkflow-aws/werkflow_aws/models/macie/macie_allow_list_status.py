from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieAllowListStatus(BaseModel):
    code: StrictStr | None = None
    description: StrictStr | None = None
