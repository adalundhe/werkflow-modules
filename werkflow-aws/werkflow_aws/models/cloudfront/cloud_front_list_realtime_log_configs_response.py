from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_realtime_log_configs import CloudFrontRealtimeLogConfigs


class CloudFrontListRealtimeLogConfigsResponse(BaseModel):
    RealtimeLogConfigs: CloudFrontRealtimeLogConfigs | None = None
    ResponseMetadata: dict[str, Any] | None = None
