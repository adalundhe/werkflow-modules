from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailUpdateBucketBundleRequest(BaseModel):
    bucketName: StrictStr
    bundleId: StrictStr
