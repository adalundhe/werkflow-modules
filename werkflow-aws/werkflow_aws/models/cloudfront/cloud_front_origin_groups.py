from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_origin_group import CloudFrontOriginGroup


class CloudFrontOriginGroups(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontOriginGroup] | None = None
