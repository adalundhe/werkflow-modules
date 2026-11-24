from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchServerlessSecurityPolicyStats(BaseModel):
    EncryptionPolicyCount: StrictInt | None = None
    NetworkPolicyCount: StrictInt | None = None
