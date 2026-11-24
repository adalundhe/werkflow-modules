from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamS3Location(BaseModel):
    S3Bucket: StrictStr | None = None
    S3Key: StrictStr | None = None
