from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteContextStoreRequest(BaseModel):
    ContextStoreId: StrictStr
