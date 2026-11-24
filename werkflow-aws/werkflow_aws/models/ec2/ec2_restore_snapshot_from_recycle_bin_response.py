from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2RestoreSnapshotFromRecycleBinResponse(BaseModel):
    SnapshotId: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    Description: StrictStr | None = None
    Encrypted: StrictBool | None = None
    OwnerId: StrictStr | None = None
    Progress: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    VolumeId: StrictStr | None = None
    VolumeSize: StrictInt | None = None
    SseType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
