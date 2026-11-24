from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeleteResourceDataSyncRequest(BaseModel):
    SyncName: StrictStr
    SyncType: StrictStr | None = None
