from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .auto_scaling_traffic_source_identifier import AutoScalingTrafficSourceIdentifier


class AutoScalingDetachTrafficSourcesRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    TrafficSources: list[AutoScalingTrafficSourceIdentifier]
