from __future__ import annotations
from pydantic import BaseModel
from .sts_origin_identity import STSOriginIdentity
from .sts_transaction_context import STSTransactionContext


class STSTrustedIdentityPropagationContext(BaseModel):
    OriginIdentity: STSOriginIdentity | None = None
    TransactionContext: STSTransactionContext | None = None
