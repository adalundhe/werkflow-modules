from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetSystemLogsForSessionRequest(BaseModel):
    Id: StrictStr
