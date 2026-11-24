from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LocationUpdateGeofenceCollectionResponse(BaseModel):
    CollectionName: StrictStr | None = None
    CollectionArn: StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
