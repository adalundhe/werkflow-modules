from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDestination(BaseModel):
    DestinationId: StrictStr | None = None
    DestinationType: StrictStr | None = None
    Status: StrictStr | None = None
