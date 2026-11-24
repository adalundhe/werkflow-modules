from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_trust_store import ELBv2TrustStore


class ELBv2CreateTrustStoreResponse(BaseModel):
    TrustStores: list[ELBv2TrustStore] | None = None
    ResponseMetadata: dict[str, Any] | None = None
