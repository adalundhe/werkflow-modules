from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteBucketAccessKeyRequest(BaseModel):
    bucketName: StrictStr
    accessKeyId: StrictStr
