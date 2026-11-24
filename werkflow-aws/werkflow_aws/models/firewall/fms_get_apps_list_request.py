from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FMSGetAppsListRequest(BaseModel):
    ListId: StrictStr
    DefaultList: StrictBool | None = None
