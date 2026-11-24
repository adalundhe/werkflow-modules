from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_traffic_mirror_target import EC2TrafficMirrorTarget


class EC2DescribeTrafficMirrorTargetsResponse(BaseModel):
    TrafficMirrorTargets: list[EC2TrafficMirrorTarget] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
