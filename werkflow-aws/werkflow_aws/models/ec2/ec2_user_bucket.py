from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2UserBucket(BaseModel):
    S3Bucket: StrictStr | None = None
    S3Key: StrictStr | None = None
