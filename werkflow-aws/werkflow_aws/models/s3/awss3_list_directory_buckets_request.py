from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3ListDirectoryBucketsRequest(BaseModel):
    ContinuationToken: StrictStr | None = None
    MaxDirectoryBuckets: StrictInt | None = None
