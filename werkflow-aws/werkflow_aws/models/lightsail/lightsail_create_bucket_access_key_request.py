from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailCreateBucketAccessKeyRequest(BaseModel):
    bucketName: StrictStr
