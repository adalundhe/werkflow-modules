from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3ListBucketsRequest(BaseModel):
    MaxBuckets: StrictInt | None = None
    ContinuationToken: StrictStr | None = None
    Prefix: StrictStr | None = None
    BucketRegion: StrictStr | None = None
