from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowSlackSourceProperties(BaseModel):
    object: StrictStr | None = None
