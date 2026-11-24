from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchPackageSource(BaseModel):
    S3BucketName: StrictStr | None = None
    S3Key: StrictStr | None = None
