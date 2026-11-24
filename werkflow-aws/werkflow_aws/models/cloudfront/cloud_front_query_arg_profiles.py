from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_query_arg_profile import CloudFrontQueryArgProfile


class CloudFrontQueryArgProfiles(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontQueryArgProfile] | None = None
