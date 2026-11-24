from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .guard_duty_shared_resource import GuardDutySharedResource


class GuardDutyObservedFindingType(BaseModel):
    FindingType: StrictStr | None = None
    Count: StrictInt | None = None
    SeverityMax: StrictFloat | StrictInt | None = None
    SharedResources: list[GuardDutySharedResource] | None = None
