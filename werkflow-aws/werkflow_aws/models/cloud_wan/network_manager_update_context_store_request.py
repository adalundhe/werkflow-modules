from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerUpdateContextStoreRequest(BaseModel):
    ContextStoreId: StrictStr
    Description: StrictStr | None = None
