from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeLogConfig(BaseModel):
    IncludeDetail: StrictStr | None = None
    Level: StrictStr | None = None
