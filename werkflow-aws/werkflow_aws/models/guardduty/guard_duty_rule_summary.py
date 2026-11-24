from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyRuleSummary(BaseModel):
    RuleId: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Severity: StrictStr | None = None
    DataSource: StrictStr | None = None
    Tactic: StrictStr | None = None
    Technique: StrictStr | None = None
    Service: StrictStr | None = None
    Language: StrictStr | None = None
    Schema: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
