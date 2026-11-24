from __future__ import annotations
from pydantic import BaseModel
from .data_sync_report_destination_s3 import DataSyncReportDestinationS3


class DataSyncReportDestination(BaseModel):
    S3: DataSyncReportDestinationS3 | None = None
