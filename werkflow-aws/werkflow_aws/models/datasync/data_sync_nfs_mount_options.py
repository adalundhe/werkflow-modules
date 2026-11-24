from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncNfsMountOptions(BaseModel):
    Version: StrictStr | None = None
