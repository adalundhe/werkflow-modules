from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_analytics_snapshot_details import KinesisAnalyticsSnapshotDetails


class KinesisAnalyticsDescribeApplicationSnapshotResponse(BaseModel):
    SnapshotDetails: KinesisAnalyticsSnapshotDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
