from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsExportSnapshotResponse(BaseModel):
    SnapshotOperationId: StrictStr | None = None
    SnapshotOperationStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
