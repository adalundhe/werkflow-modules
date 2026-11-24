from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .guard_duty_shared_behavior import GuardDutySharedBehavior
from .guard_duty_shared_resource import GuardDutySharedResource


class GuardDutyCorrelatedFinding(BaseModel):
    FindingType: StrictStr | None = None
    Count: StrictInt | None = None
    SeverityMax: StrictFloat | StrictInt | None = None
    CorrelationReasons: list[StrictStr] | None = None
    FindingIds: list[StrictStr] | None = None
    SharedResources: list[GuardDutySharedResource] | None = None
    SharedBehaviors: list[GuardDutySharedBehavior] | None = None
