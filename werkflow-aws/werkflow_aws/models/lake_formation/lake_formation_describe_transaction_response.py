from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lake_formation_transaction_description import LakeFormationTransactionDescription


class LakeFormationDescribeTransactionResponse(BaseModel):
    TransactionDescription: LakeFormationTransactionDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
