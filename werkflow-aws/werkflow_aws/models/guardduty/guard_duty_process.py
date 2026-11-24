from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_finding_reference import GuardDutyFindingReference


class GuardDutyProcess(BaseModel):
    Uuid: StrictStr | None = None
    Name: StrictStr | None = None
    Path: StrictStr | None = None
    ParentUuid: StrictStr | None = None
    Findings: list[GuardDutyFindingReference] | None = None
