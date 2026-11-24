from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_tags import CloudFrontTags


class CloudFrontTagResourceRequest(BaseModel):
    Resource: StrictStr
    Tags: CloudFrontTags
