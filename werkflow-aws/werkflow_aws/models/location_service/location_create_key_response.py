from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LocationCreateKeyResponse(BaseModel):
    Key: StrictStr | None = None
    KeyArn: StrictStr | None = None
    KeyName: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
