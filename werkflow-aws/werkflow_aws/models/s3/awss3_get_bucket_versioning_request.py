from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3GetBucketVersioningRequest(BaseModel):
    Bucket: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
