from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyOwner(BaseModel):
    Id: StrictStr | None = None
