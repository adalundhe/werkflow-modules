from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsSnapshotOperationInfo(BaseModel):
    SnapshotOperationId: StrictStr | None = None
    SnapshotOperation: StrictStr | None = None
    SnapshotOperationStatus: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
