from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowServiceNowSourceProperties(BaseModel):
    object: StrictStr | None = None
