from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowZendeskSourceProperties(BaseModel):
    object: StrictStr | None = None
