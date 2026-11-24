from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2ModifyTrustStoreRequest(BaseModel):
    TrustStoreArn: StrictStr
    CaCertificatesBundleS3Bucket: StrictStr
    CaCertificatesBundleS3Key: StrictStr
    CaCertificatesBundleS3ObjectVersion: StrictStr | None = None
