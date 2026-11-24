from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_trust_store import ELBv2TrustStore


class ELBv2DescribeTrustStoresResponse(BaseModel):
    TrustStores: list[ELBv2TrustStore] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
