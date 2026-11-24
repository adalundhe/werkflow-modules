from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .guard_duty_destination_properties import GuardDutyDestinationProperties


class GuardDutyCreatePublishingDestinationRequest(BaseModel):
    DetectorId: StrictStr
    DestinationType: Literal['S3']
    DestinationProperties: GuardDutyDestinationProperties
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
