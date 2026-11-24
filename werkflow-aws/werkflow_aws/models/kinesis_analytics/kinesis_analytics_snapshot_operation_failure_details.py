from __future__ import annotations
from pydantic import BaseModel
from .kinesis_analytics_snapshot_error_info import KinesisAnalyticsSnapshotErrorInfo


class KinesisAnalyticsSnapshotOperationFailureDetails(BaseModel):
    ErrorInfo: KinesisAnalyticsSnapshotErrorInfo | None = None
