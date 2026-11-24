from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .backup_report_delivery_channel import BackupReportDeliveryChannel
from .backup_report_setting import BackupReportSetting


class BackupReportPlan(BaseModel):
    ReportPlanArn: StrictStr | None = None
    ReportPlanName: StrictStr | None = None
    ReportPlanDescription: StrictStr | None = None
    ReportSetting: BackupReportSetting | None = None
    ReportDeliveryChannel: BackupReportDeliveryChannel | None = None
    DeploymentStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastAttemptedExecutionTime: datetime.datetime | StrictStr | None = None
    LastSuccessfulExecutionTime: datetime.datetime | StrictStr | None = None
