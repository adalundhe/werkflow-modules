from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_report_destination import DataSyncReportDestination
from .data_sync_report_overrides import DataSyncReportOverrides


class DataSyncTaskReportConfig(BaseModel):
    Destination: DataSyncReportDestination | None = None
    OutputType: StrictStr | None = None
    ReportLevel: StrictStr | None = None
    ObjectVersionIds: StrictStr | None = None
    Overrides: DataSyncReportOverrides | None = None
