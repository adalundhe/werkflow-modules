from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessStreamBucketConfig(BaseModel):
    bucket: StrictStr | None = None
    bucketOwnerAccountId: StrictStr | None = None
    initialScan: StrictStr | None = None
