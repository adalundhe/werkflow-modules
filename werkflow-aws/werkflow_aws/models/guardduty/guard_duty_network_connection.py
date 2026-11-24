from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyNetworkConnection(BaseModel):
    Direction: StrictStr | None = None
