from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowZendeskMetadata(BaseModel):
    oAuthScopes: list[StrictStr] | None = None
