from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationExtendTransactionRequest(BaseModel):
    TransactionId: StrictStr | None = None
