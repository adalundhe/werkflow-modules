from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_investigation_summary import GuardDutyInvestigationSummary


class GuardDutyListInvestigationsResponse(BaseModel):
    Investigations: list[GuardDutyInvestigationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
