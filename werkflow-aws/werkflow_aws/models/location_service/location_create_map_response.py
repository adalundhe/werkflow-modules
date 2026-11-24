from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LocationCreateMapResponse(BaseModel):
    MapName: StrictStr | None = None
    MapArn: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
