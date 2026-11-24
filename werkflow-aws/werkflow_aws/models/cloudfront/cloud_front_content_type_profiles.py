from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_content_type_profile import CloudFrontContentTypeProfile


class CloudFrontContentTypeProfiles(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontContentTypeProfile] | None = None
