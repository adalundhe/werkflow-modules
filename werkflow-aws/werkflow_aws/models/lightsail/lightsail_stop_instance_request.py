from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailStopInstanceRequest(BaseModel):
    instanceName: StrictStr
    force: StrictBool | None = None
