from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointJourneyCustomMessage(BaseModel):
    Data: StrictStr | None = None
