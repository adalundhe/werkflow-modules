from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3DeletePublicAccessBlockRequest(BaseModel):
    Bucket: StrictStr
    ExpectedBucketOwner: StrictStr | None = None
