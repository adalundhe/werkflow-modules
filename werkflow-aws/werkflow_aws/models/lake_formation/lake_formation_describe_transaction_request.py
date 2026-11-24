from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDescribeTransactionRequest(BaseModel):
    TransactionId: StrictStr
