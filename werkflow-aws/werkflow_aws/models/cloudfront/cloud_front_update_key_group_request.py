from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_key_group_config import CloudFrontKeyGroupConfig


class CloudFrontUpdateKeyGroupRequest(BaseModel):
    KeyGroupConfig: CloudFrontKeyGroupConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None
