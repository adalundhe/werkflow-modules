from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LightsailGetBucketBundlesRequest(BaseModel):
    includeInactive: StrictBool | None = None
