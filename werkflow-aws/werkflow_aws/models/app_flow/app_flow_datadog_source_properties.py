from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowDatadogSourceProperties(BaseModel):
    object: StrictStr | None = None
