from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_investigation_resource_data import GuardDutyInvestigationResourceData


class GuardDutyInvestigationResource(BaseModel):
    Uid: StrictStr | None = None
    Name: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Data: GuardDutyInvestigationResourceData | None = None
