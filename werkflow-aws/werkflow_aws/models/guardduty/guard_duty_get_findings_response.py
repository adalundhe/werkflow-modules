from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_finding import GuardDutyFinding


class GuardDutyGetFindingsResponse(BaseModel):
    Findings: list[GuardDutyFinding] | None = None
    ResponseMetadata: dict[str, Any] | None = None
