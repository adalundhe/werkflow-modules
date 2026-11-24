from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3GetBucketMetricsConfigurationRequest(BaseModel):
    Bucket: StrictStr
    Id: StrictStr
    ExpectedBucketOwner: StrictStr | None = None
