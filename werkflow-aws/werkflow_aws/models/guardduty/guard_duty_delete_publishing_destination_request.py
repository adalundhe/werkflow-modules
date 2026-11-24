from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDeletePublishingDestinationRequest(BaseModel):
    DetectorId: StrictStr
    DestinationId: StrictStr
