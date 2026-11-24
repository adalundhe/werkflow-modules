from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glacier_data_retrieval_policy import GlacierDataRetrievalPolicy


class GlacierSetDataRetrievalPolicyRequest(BaseModel):
    accountId: StrictStr
    Policy: GlacierDataRetrievalPolicy | None = None
