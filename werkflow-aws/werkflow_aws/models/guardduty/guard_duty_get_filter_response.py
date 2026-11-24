from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_finding_criteria import GuardDutyFindingCriteria


class GuardDutyGetFilterResponse(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Action: StrictStr | None = None
    Rank: StrictInt | None = None
    FindingCriteria: GuardDutyFindingCriteria | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Version: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
