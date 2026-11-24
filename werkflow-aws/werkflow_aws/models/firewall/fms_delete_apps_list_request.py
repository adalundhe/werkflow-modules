from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSDeleteAppsListRequest(BaseModel):
    ListId: StrictStr
