from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsSnapshotInfo(BaseModel):
    SnapshotName: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
    SnapshotStatus: StrictStr | None = None
    SnapshotCreationTimestamp: datetime.datetime | StrictStr | None = None
    SnapshotInitiator: StrictStr | None = None
    SnapshotInitiatorOperation: StrictStr | None = None
    SourceApplicationName: StrictStr | None = None
    SnapshotFormat: StrictStr | None = None
