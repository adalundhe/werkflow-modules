from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LocationCreateGeofenceCollectionResponse(BaseModel):
    CollectionName: StrictStr | None = None
    CollectionArn: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
