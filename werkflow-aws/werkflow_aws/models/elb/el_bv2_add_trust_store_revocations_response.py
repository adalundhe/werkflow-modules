from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_trust_store_revocation import ELBv2TrustStoreRevocation


class ELBv2AddTrustStoreRevocationsResponse(BaseModel):
    TrustStoreRevocations: list[ELBv2TrustStoreRevocation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
