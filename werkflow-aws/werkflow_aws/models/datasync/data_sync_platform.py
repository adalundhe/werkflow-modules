from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncPlatform(BaseModel):
    Version: StrictStr | None = None
