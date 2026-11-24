from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_tag_keys import CloudFrontTagKeys


class CloudFrontUntagResourceRequest(BaseModel):
    Resource: StrictStr
    TagKeys: CloudFrontTagKeys
