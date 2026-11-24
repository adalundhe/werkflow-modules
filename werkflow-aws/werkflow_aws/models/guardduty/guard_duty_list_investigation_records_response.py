from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_investigation_record import GuardDutyInvestigationRecord


class GuardDutyListInvestigationRecordsResponse(BaseModel):
    InvestigationId: StrictStr | None = None
    Status: StrictStr | None = None
    Records: list[GuardDutyInvestigationRecord] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
