from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3ListBucketAnalyticsConfigurationsRequest(BaseModel):
    Bucket: StrictStr
    ContinuationToken: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
