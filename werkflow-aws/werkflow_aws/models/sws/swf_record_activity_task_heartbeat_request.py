from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFRecordActivityTaskHeartbeatRequest(BaseModel):
    taskToken: StrictStr
    details: StrictStr | None = None
