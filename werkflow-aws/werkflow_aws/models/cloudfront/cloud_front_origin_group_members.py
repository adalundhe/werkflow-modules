from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_origin_group_member import CloudFrontOriginGroupMember


class CloudFrontOriginGroupMembers(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontOriginGroupMember] | None = None
