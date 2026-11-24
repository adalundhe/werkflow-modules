from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierGetVaultAccessPolicyRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
