from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .cloud_front_query_arg_profiles import CloudFrontQueryArgProfiles


class CloudFrontQueryArgProfileConfig(BaseModel):
    ForwardWhenQueryArgProfileIsUnknown: StrictBool | None = None
    QueryArgProfiles: CloudFrontQueryArgProfiles | None = None
