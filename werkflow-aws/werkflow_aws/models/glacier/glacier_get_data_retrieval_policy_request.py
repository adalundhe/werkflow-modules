from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierGetDataRetrievalPolicyRequest(BaseModel):
    accountId: StrictStr
