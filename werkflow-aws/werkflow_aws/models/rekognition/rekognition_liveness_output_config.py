from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionLivenessOutputConfig(BaseModel):
    S3Bucket: StrictStr
    S3KeyPrefix: StrictStr | None = None
