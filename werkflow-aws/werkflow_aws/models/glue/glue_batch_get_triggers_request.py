from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchGetTriggersRequest(BaseModel):
    TriggerNames: list[StrictStr]
