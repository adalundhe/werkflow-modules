from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyDetectionRuleOrgConfiguration(BaseModel):
    RuleId: StrictStr | None = None
    Mode: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    IncludeAccountIds: list[StrictStr] | None = None
    ExcludeAccountIds: list[StrictStr] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ExpiresAt: datetime.datetime | StrictStr | None = None
