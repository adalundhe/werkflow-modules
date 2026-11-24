from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3GetBucketNotificationConfigurationRequest(BaseModel):
    Bucket: StrictStr
    ExpectedBucketOwner: StrictStr | None = None
