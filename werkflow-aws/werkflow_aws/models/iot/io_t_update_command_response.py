from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class IoTUpdateCommandResponse(BaseModel):
    commandId: StrictStr | None = None
    displayName: StrictStr | None = None
    description: StrictStr | None = None
    deprecated: StrictBool | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
