from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_traffic_mirror_session import EC2TrafficMirrorSession


class EC2ModifyTrafficMirrorSessionResponse(BaseModel):
    TrafficMirrorSession: EC2TrafficMirrorSession | None = None
    ResponseMetadata: dict[str, Any] | None = None
