from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeReportJobRequest(BaseModel):
    ReportJobId: StrictStr
