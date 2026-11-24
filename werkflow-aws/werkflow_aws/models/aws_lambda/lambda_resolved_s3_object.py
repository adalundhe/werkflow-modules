from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaResolvedS3Object(BaseModel):
    S3Bucket: StrictStr | None = None
    S3Key: StrictStr | None = None
    S3ObjectVersion: StrictStr | None = None
