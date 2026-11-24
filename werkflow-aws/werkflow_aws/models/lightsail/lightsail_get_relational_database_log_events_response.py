from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_log_event import LightsailLogEvent


class LightsailGetRelationalDatabaseLogEventsResponse(BaseModel):
    resourceLogEvents: list[LightsailLogEvent] | None = None
    nextBackwardToken: StrictStr | None = None
    nextForwardToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
