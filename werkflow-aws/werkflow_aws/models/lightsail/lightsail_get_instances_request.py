from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailGetInstancesRequest(BaseModel):
    pageToken: StrictStr | None = None
    includeHealthStatus: StrictBool | None = None
