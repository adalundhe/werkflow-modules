from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncQopConfiguration(BaseModel):
    RpcProtection: StrictStr | None = None
    DataTransferProtection: StrictStr | None = None
