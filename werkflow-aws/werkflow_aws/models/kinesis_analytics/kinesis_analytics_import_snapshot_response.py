from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsImportSnapshotResponse(BaseModel):
    SnapshotArn: StrictStr | None = None
    SnapshotStatus: StrictStr | None = None
    SnapshotOperationId: StrictStr | None = None
    SnapshotOperationStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
