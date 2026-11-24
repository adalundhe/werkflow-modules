from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3GetBucketMetadataTableConfigurationRequest(BaseModel):
    Bucket: StrictStr
    ExpectedBucketOwner: StrictStr | None = None
