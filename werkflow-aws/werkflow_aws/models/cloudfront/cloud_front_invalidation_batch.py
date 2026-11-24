from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_paths import CloudFrontPaths


class CloudFrontInvalidationBatch(BaseModel):
    Paths: CloudFrontPaths | None = None
    CallerReference: StrictStr | None = None
