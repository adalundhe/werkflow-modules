from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_traffic_mirror_filter_rule import EC2TrafficMirrorFilterRule


class EC2DescribeTrafficMirrorFilterRulesResponse(BaseModel):
    TrafficMirrorFilterRules: list[EC2TrafficMirrorFilterRule] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
