from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_front_realtime_log_config import CloudFrontRealtimeLogConfig


class CloudFrontRealtimeLogConfigs(BaseModel):
    MaxItems: StrictInt | None = None
    Items: list[CloudFrontRealtimeLogConfig] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    NextMarker: StrictStr | None = None
