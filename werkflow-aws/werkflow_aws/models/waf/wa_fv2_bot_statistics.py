from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class WAFv2BotStatistics(BaseModel):
    BotName: StrictStr | None = None
    RequestCount: StrictInt | None = None
    Percentage: StrictFloat | StrictInt | None = None
