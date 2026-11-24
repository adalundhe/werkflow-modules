from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierDescribeVaultRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
