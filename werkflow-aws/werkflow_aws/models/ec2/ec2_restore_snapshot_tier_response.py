from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2RestoreSnapshotTierResponse(BaseModel):
    SnapshotId: StrictStr | None = None
    RestoreStartTime: datetime.datetime | StrictStr | None = None
    RestoreDuration: StrictInt | None = None
    IsPermanentRestore: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
