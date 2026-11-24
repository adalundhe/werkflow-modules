from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontTrustStoreConfig(BaseModel):
    TrustStoreId: StrictStr | None = None
    AdvertiseTrustStoreCaNames: StrictBool | None = None
    IgnoreCertificateExpiry: StrictBool | None = None
