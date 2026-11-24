from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessIngestionJobS3Source(BaseModel):
    bucket: StrictStr | None = None
    bucketOwnerAccountId: StrictStr | None = None
    keyPrefix: StrictStr | None = None
