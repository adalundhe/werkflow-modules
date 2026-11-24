from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_key_group_config import CloudFrontKeyGroupConfig


class CloudFrontGetKeyGroupConfigResponse(BaseModel):
    KeyGroupConfig: CloudFrontKeyGroupConfig | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
