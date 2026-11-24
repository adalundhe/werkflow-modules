from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3DeleteObjectTaggingRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    VersionId: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
