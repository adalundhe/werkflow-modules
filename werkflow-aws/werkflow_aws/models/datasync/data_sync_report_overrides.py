from __future__ import annotations
from pydantic import BaseModel
from .data_sync_report_override import DataSyncReportOverride


class DataSyncReportOverrides(BaseModel):
    Transferred: DataSyncReportOverride | None = None
    Verified: DataSyncReportOverride | None = None
    Deleted: DataSyncReportOverride | None = None
    Skipped: DataSyncReportOverride | None = None
