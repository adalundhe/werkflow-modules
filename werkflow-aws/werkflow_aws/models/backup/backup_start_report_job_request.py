from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupStartReportJobRequest(BaseModel):
    ReportPlanName: StrictStr
    IdempotencyToken: StrictStr | None = None
