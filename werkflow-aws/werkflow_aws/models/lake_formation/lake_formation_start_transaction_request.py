from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LakeFormationStartTransactionRequest(BaseModel):
    TransactionType: Literal['READ_AND_WRITE', 'READ_ONLY'] | None = None
