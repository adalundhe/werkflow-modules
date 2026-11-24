from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class EC2LockSnapshotResponse(BaseModel):
    SnapshotId: StrictStr | None = None
    LockState: StrictStr | None = None
    LockDuration: StrictInt | None = None
    CoolOffPeriod: StrictInt | None = None
    CoolOffPeriodExpiresOn: datetime.datetime | StrictStr | None = None
    LockCreatedOn: datetime.datetime | StrictStr | None = None
    LockExpiresOn: datetime.datetime | StrictStr | None = None
    LockDurationStartTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
