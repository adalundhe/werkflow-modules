from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_key_group import CloudFrontKeyGroup


class CloudFrontKeyGroupSummary(BaseModel):
    KeyGroup: CloudFrontKeyGroup | None = None
