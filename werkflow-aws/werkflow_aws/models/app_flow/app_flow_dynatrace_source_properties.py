from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowDynatraceSourceProperties(BaseModel):
    object: StrictStr | None = None
