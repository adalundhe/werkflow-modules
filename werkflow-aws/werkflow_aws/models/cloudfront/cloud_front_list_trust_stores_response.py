from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_trust_store_summary import CloudFrontTrustStoreSummary


class CloudFrontListTrustStoresResponse(BaseModel):
    NextMarker: StrictStr | None = None
    TrustStoreList: list[CloudFrontTrustStoreSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
