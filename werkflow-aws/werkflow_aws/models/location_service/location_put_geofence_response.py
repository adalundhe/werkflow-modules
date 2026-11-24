from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LocationPutGeofenceResponse(BaseModel):
    GeofenceId: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
