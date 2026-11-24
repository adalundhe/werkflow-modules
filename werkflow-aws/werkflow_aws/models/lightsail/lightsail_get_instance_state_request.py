from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetInstanceStateRequest(BaseModel):
    instanceName: StrictStr
