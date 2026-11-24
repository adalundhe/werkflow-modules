from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .x_ray_cloud_watch_logs_configuration import XRayCloudWatchLogsConfiguration


class XRayUpdateTraceSegmentDestinationRequest(BaseModel):
    Destination: Literal['XRay', 'CloudWatchLogs'] | None = None
    CloudWatchLogsConfiguration: XRayCloudWatchLogsConfiguration | None = None
