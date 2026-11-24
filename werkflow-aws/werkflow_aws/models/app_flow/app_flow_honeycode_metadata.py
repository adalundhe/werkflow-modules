from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowHoneycodeMetadata(BaseModel):
    oAuthScopes: list[StrictStr] | None = None
