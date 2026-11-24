from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetBucketAccessKeysRequest(BaseModel):
    bucketName: StrictStr
