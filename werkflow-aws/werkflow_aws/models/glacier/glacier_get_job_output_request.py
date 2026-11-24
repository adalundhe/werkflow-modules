from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierGetJobOutputRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    jobId: StrictStr
    range: StrictStr | None = None
