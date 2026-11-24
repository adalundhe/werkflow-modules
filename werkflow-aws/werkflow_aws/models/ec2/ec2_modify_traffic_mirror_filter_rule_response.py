from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_traffic_mirror_filter_rule import EC2TrafficMirrorFilterRule


class EC2ModifyTrafficMirrorFilterRuleResponse(BaseModel):
    TrafficMirrorFilterRule: EC2TrafficMirrorFilterRule | None = None
    ResponseMetadata: dict[str, Any] | None = None
