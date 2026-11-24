from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_traffic_source_state import AutoScalingTrafficSourceState


class AutoScalingDescribeTrafficSourcesResponse(BaseModel):
    TrafficSources: list[AutoScalingTrafficSourceState] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
