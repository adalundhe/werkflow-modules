from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_open_hours_rule import PinpointOpenHoursRule


class PinpointOpenHours(BaseModel):
    EMAIL: dict[StrictStr, list[PinpointOpenHoursRule]] | None = None
    SMS: dict[StrictStr, list[PinpointOpenHoursRule]] | None = None
    PUSH: dict[StrictStr, list[PinpointOpenHoursRule]] | None = None
    VOICE: dict[StrictStr, list[PinpointOpenHoursRule]] | None = None
    CUSTOM: dict[StrictStr, list[PinpointOpenHoursRule]] | None = None
