from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_trust_store_config import CloudFrontTrustStoreConfig


class CloudFrontViewerMtlsConfig(BaseModel):
    Mode: StrictStr | None = None
    TrustStoreConfig: CloudFrontTrustStoreConfig | None = None
