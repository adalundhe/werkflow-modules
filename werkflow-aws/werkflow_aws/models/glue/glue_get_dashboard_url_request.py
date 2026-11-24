from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueGetDashboardUrlRequest(BaseModel):
    ResourceId: StrictStr
    ResourceType: Literal['JOB', 'SESSION']
    RequestOrigin: StrictStr | None = None
