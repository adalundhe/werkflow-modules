from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetContextVersionRequest(BaseModel):
    ContextStoreId: StrictStr
