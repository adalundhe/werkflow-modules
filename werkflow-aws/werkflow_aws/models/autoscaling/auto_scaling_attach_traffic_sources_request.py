from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .auto_scaling_traffic_source_identifier import AutoScalingTrafficSourceIdentifier


class AutoScalingAttachTrafficSourcesRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    TrafficSources: list[AutoScalingTrafficSourceIdentifier]
    SkipZonalShiftValidation: StrictBool | None = None
