from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailGenerateQueryRequest(BaseModel):
    EventDataStores: list[StrictStr]
    Prompt: StrictStr
