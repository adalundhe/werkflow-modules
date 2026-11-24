from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneAssetOwnershipTransfer(BaseModel):
    status: StrictStr | None = None
    sourceProjectId: StrictStr | None = None
    targetProjectId: StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
