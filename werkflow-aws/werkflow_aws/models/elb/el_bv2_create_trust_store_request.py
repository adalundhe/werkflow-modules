from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_tag import ELBv2Tag


class ELBv2CreateTrustStoreRequest(BaseModel):
    Name: StrictStr
    CaCertificatesBundleS3Bucket: StrictStr
    CaCertificatesBundleS3Key: StrictStr
    CaCertificatesBundleS3ObjectVersion: StrictStr | None = None
    Tags: list[ELBv2Tag] | None = None
