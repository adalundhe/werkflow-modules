from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowSlackMetadata(BaseModel):
    oAuthScopes: list[StrictStr] | None = None
