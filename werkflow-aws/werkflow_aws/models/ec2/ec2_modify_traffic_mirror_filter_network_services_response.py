from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_traffic_mirror_filter import EC2TrafficMirrorFilter


class EC2ModifyTrafficMirrorFilterNetworkServicesResponse(BaseModel):
    TrafficMirrorFilter: EC2TrafficMirrorFilter | None = None
    ResponseMetadata: dict[str, Any] | None = None
