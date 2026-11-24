from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRStopReplicationBackfillRequest(BaseModel):
    replicationBackfillId: StrictStr
    registryId: StrictStr | None = None
