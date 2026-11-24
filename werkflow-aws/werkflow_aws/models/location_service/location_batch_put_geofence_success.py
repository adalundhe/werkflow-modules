from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LocationBatchPutGeofenceSuccess(BaseModel):
    GeofenceId: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
