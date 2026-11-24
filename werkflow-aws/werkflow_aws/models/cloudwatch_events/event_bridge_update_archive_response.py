from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EventBridgeUpdateArchiveResponse(BaseModel):
    ArchiveArn: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
