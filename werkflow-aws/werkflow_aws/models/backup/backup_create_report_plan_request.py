from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_report_delivery_channel import BackupReportDeliveryChannel
from .backup_report_setting import BackupReportSetting


class BackupCreateReportPlanRequest(BaseModel):
    ReportPlanName: StrictStr
    ReportDeliveryChannel: BackupReportDeliveryChannel
    ReportSetting: BackupReportSetting
    ReportPlanDescription: StrictStr | None = None
    ReportPlanTags: dict[StrictStr, StrictStr] | None = None
    IdempotencyToken: StrictStr | None = None
