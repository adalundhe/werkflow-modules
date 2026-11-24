from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_describe_trust_store_revocation import ELBv2DescribeTrustStoreRevocation


class ELBv2DescribeTrustStoreRevocationsResponse(BaseModel):
    TrustStoreRevocations: list[ELBv2DescribeTrustStoreRevocation] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
