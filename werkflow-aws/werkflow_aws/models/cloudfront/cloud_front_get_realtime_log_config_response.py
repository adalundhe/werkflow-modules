from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_realtime_log_config import CloudFrontRealtimeLogConfig


class CloudFrontGetRealtimeLogConfigResponse(BaseModel):
    RealtimeLogConfig: CloudFrontRealtimeLogConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
