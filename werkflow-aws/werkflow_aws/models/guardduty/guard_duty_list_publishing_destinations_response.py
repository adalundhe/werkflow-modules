from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_destination import GuardDutyDestination


class GuardDutyListPublishingDestinationsResponse(BaseModel):
    Destinations: list[GuardDutyDestination] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
