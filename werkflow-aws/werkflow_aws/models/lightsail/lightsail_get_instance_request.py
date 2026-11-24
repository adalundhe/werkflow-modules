from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailGetInstanceRequest(BaseModel):
    instanceName: StrictStr
    includeHealthStatus: StrictBool | None = None
