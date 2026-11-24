from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_resource_data import GuardDutyResourceData
from .guard_duty_tag import GuardDutyTag


class GuardDutyResourceV2(BaseModel):
    Uid: StrictStr | None = None
    Name: StrictStr | None = None
    AccountId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Region: StrictStr | None = None
    Service: StrictStr | None = None
    CloudPartition: StrictStr | None = None
    Tags: list[GuardDutyTag] | None = None
    Data: GuardDutyResourceData | None = None
