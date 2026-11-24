from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsListSnapshotOperationsRequest(BaseModel):
    SnapshotName: StrictStr
    SnapshotOperation: Literal['CreateSnapshot', 'DeleteSnapshot', 'ImportSnapshot', 'ExportSnapshot', 'SystemCreateSnapshot'] | None = None
    SnapshotOperationStatus: Literal['IN_PROGRESS', 'SUCCESSFUL', 'FAILED', 'CANCELLED'] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
