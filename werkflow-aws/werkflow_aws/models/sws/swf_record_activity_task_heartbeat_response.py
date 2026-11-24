from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool


class SWFRecordActivityTaskHeartbeatResponse(BaseModel):
    cancelRequested: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
