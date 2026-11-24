from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2ModifySnapshotTierResponse(BaseModel):
    SnapshotId: StrictStr | None = None
    TieringStartTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
