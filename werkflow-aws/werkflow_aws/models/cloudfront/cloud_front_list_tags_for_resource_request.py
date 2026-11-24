from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListTagsForResourceRequest(BaseModel):
    Resource: StrictStr
