from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_key_group_config import CloudFrontKeyGroupConfig


class CloudFrontCreateKeyGroupRequest(BaseModel):
    KeyGroupConfig: CloudFrontKeyGroupConfig
