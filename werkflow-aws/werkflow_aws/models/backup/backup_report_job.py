from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .backup_report_destination import BackupReportDestination


class BackupReportJob(BaseModel):
    ReportJobId: StrictStr | None = None
    ReportPlanArn: StrictStr | None = None
    ReportTemplate: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    ReportDestination: BackupReportDestination | None = None
