from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDescribePublishingDestinationRequest(BaseModel):
    DetectorId: StrictStr
    DestinationId: StrictStr
