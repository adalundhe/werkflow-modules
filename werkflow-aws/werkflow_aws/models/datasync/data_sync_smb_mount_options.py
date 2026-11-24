from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncSmbMountOptions(BaseModel):
    Version: StrictStr | None = None
