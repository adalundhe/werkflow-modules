from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_report_plan import BackupReportPlan


class BackupListReportPlansResponse(BaseModel):
    ReportPlans: list[BackupReportPlan] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
