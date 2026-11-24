from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowSingularSourceProperties(BaseModel):
    object: StrictStr | None = None
