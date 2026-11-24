from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_snapshot_details import KinesisAnalyticsSnapshotDetails


class KinesisAnalyticsListApplicationSnapshotsResponse(BaseModel):
    SnapshotSummaries: list[KinesisAnalyticsSnapshotDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
