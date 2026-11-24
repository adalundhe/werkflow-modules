from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LocationUpdatePlaceIndexResponse(BaseModel):
    IndexName: StrictStr | None = None
    IndexArn: StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
