from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3AnalyticsS3BucketDestination(BaseModel):
    Format: StrictStr | None = None
    BucketAccountId: StrictStr | None = None
    Bucket: StrictStr | None = None
    Prefix: StrictStr | None = None
