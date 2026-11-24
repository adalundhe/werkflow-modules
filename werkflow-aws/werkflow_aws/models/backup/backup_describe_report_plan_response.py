from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .backup_report_plan import BackupReportPlan


class BackupDescribeReportPlanResponse(BaseModel):
    ReportPlan: BackupReportPlan | None = None
    ResponseMetadata: dict[str, Any] | None = None
