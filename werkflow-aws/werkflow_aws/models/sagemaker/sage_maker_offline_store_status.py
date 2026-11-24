from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOfflineStoreStatus(BaseModel):
    Status: StrictStr | None = None
    BlockedReason: StrictStr | None = None
