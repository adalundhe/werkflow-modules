from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupScheduledPlanExecutionMember(BaseModel):
    ExecutionTime: datetime.datetime | StrictStr | None = None
    RuleId: StrictStr | None = None
    RuleExecutionType: StrictStr | None = None
