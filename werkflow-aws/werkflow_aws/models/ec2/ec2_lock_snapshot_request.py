from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2LockSnapshotRequest(BaseModel):
    SnapshotId: StrictStr
    LockMode: Literal['compliance', 'governance']
    DryRun: StrictBool | None = None
    CoolOffPeriod: StrictInt | None = None
    LockDuration: StrictInt | None = None
    ExpirationDate: datetime.datetime | StrictStr | None = None
