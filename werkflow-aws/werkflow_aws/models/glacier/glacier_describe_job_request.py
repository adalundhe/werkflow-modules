from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierDescribeJobRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    jobId: StrictStr
