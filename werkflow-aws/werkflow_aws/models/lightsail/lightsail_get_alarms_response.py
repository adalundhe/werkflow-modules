from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_alarm import LightsailAlarm


class LightsailGetAlarmsResponse(BaseModel):
    alarms: list[LightsailAlarm] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
