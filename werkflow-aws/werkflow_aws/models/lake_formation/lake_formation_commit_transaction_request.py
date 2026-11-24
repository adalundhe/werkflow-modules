from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationCommitTransactionRequest(BaseModel):
    TransactionId: StrictStr
