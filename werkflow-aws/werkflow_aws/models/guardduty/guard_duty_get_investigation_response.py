from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_investigation import GuardDutyInvestigation


class GuardDutyGetInvestigationResponse(BaseModel):
    Investigation: GuardDutyInvestigation | None = None
    ResponseMetadata: dict[str, Any] | None = None
