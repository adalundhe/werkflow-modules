from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsListSnapshotsRequest(BaseModel):
    SourceApplicationName: StrictStr | None = None
    SnapshotInitiator: Literal['USER', 'SYSTEM'] | None = None
    SnapshotInitiatorOperation: Literal['CreateSnapshot', 'ImportSnapshot', 'SystemCreateSnapshot'] | None = None
    SnapshotStatus: Literal['CREATING', 'READY', 'DELETING', 'FAILED'] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
