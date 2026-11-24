from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeReportPlanRequest(BaseModel):
    ReportPlanName: StrictStr
