from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_trust_store import CloudFrontTrustStore


class CloudFrontCreateTrustStoreResponse(BaseModel):
    TrustStore: CloudFrontTrustStore | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
