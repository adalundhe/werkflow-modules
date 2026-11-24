from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_analytics_snapshot_info_details import KinesisAnalyticsSnapshotInfoDetails


class KinesisAnalyticsDescribeSnapshotResponse(BaseModel):
    SnapshotInfoDetails: KinesisAnalyticsSnapshotInfoDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
