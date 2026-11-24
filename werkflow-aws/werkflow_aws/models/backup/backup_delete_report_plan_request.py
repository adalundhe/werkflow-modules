from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDeleteReportPlanRequest(BaseModel):
    ReportPlanName: StrictStr
