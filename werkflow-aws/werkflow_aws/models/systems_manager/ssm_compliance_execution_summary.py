from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMComplianceExecutionSummary(BaseModel):
    ExecutionTime: datetime.datetime | StrictStr | None = None
    ExecutionId: StrictStr | None = None
    ExecutionType: StrictStr | None = None
