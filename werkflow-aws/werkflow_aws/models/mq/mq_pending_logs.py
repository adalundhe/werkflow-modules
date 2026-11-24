from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MQPendingLogs(BaseModel):
    Audit: StrictBool | None = None
    General: StrictBool | None = None
