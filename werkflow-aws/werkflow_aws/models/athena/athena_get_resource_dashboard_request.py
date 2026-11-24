from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaGetResourceDashboardRequest(BaseModel):
    ResourceARN: StrictStr
