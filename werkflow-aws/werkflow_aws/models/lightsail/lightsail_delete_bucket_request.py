from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailDeleteBucketRequest(BaseModel):
    bucketName: StrictStr
    forceDelete: StrictBool | None = None
