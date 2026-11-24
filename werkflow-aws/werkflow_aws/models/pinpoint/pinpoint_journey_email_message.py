from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointJourneyEmailMessage(BaseModel):
    FromAddress: StrictStr | None = None
