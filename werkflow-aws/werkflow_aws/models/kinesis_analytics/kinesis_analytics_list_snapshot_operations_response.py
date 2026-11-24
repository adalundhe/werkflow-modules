from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_snapshot_operation_info import KinesisAnalyticsSnapshotOperationInfo


class KinesisAnalyticsListSnapshotOperationsResponse(BaseModel):
    SnapshotOperationInfoList: list[KinesisAnalyticsSnapshotOperationInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
