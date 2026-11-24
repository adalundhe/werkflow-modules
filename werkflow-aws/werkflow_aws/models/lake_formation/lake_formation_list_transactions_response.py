from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_transaction_description import LakeFormationTransactionDescription


class LakeFormationListTransactionsResponse(BaseModel):
    Transactions: list[LakeFormationTransactionDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
