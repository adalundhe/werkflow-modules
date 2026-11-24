from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .cloud_front_content_type_profiles import CloudFrontContentTypeProfiles


class CloudFrontContentTypeProfileConfig(BaseModel):
    ForwardWhenContentTypeIsUnknown: StrictBool | None = None
    ContentTypeProfiles: CloudFrontContentTypeProfiles | None = None
