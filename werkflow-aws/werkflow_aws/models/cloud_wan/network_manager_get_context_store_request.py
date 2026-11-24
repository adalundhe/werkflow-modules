from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetContextStoreRequest(BaseModel):
    ContextStoreId: StrictStr
