from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationCancelTransactionRequest(BaseModel):
    TransactionId: StrictStr
