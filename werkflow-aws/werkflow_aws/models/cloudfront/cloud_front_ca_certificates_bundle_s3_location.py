from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontCaCertificatesBundleS3Location(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    Region: StrictStr
    Version: StrictStr | None = None
