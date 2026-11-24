from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceSourceDetail(BaseModel):
    EventSource: StrictStr | None = None
    MessageType: StrictStr | None = None
    MaximumExecutionFrequency: StrictStr | None = None
