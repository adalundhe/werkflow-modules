from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2SnapshotRecycleBinInfo(BaseModel):
    SnapshotId: StrictStr | None = None
    RecycleBinEnterTime: datetime.datetime | StrictStr | None = None
    RecycleBinExitTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    VolumeId: StrictStr | None = None
