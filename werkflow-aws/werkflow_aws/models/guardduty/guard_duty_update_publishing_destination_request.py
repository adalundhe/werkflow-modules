from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_destination_properties import GuardDutyDestinationProperties


class GuardDutyUpdatePublishingDestinationRequest(BaseModel):
    DetectorId: StrictStr
    DestinationId: StrictStr
    DestinationProperties: GuardDutyDestinationProperties | None = None
