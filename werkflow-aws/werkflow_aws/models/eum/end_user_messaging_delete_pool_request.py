from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeletePoolRequest(BaseModel):
    PoolId: StrictStr
