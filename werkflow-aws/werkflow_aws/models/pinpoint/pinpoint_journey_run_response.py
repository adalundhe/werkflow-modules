from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointJourneyRunResponse(BaseModel):
    CreationTime: StrictStr | None = None
    LastUpdateTime: StrictStr | None = None
    RunId: StrictStr | None = None
    Status: StrictStr | None = None
