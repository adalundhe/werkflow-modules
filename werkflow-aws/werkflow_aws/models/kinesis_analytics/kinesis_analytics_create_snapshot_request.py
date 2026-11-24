from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_tag import KinesisAnalyticsTag


class KinesisAnalyticsCreateSnapshotRequest(BaseModel):
    ApplicationName: StrictStr
    SnapshotName: StrictStr
    SnapshotDescription: StrictStr | None = None
    Tags: list[KinesisAnalyticsTag] | None = None
