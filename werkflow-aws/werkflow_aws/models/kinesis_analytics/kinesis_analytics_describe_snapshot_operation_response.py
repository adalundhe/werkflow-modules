from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_analytics_snapshot_operation_info_details import KinesisAnalyticsSnapshotOperationInfoDetails


class KinesisAnalyticsDescribeSnapshotOperationResponse(BaseModel):
    SnapshotOperationInfoDetails: KinesisAnalyticsSnapshotOperationInfoDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
