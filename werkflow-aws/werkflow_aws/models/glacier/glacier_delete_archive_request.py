from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierDeleteArchiveRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    archiveId: StrictStr
