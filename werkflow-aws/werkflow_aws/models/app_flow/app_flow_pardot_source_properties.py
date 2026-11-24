from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowPardotSourceProperties(BaseModel):
    object: StrictStr | None = None
