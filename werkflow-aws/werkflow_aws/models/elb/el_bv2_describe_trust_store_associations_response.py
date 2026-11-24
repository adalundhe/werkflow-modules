from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_trust_store_association import ELBv2TrustStoreAssociation


class ELBv2DescribeTrustStoreAssociationsResponse(BaseModel):
    TrustStoreAssociations: list[ELBv2TrustStoreAssociation] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
