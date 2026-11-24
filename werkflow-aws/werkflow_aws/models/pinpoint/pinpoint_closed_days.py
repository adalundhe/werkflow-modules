from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_closed_days_rule import PinpointClosedDaysRule


class PinpointClosedDays(BaseModel):
    EMAIL: list[PinpointClosedDaysRule] | None = None
    SMS: list[PinpointClosedDaysRule] | None = None
    PUSH: list[PinpointClosedDaysRule] | None = None
    VOICE: list[PinpointClosedDaysRule] | None = None
    CUSTOM: list[PinpointClosedDaysRule] | None = None
