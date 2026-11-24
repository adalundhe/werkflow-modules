from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_report_delivery_channel import BackupReportDeliveryChannel
from .backup_report_setting import BackupReportSetting


class BackupUpdateReportPlanRequest(BaseModel):
    ReportPlanName: StrictStr
    ReportPlanDescription: StrictStr | None = None
    ReportDeliveryChannel: BackupReportDeliveryChannel | None = None
    ReportSetting: BackupReportSetting | None = None
    IdempotencyToken: StrictStr | None = None
