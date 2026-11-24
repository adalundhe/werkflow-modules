from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_traffic_mirror_filter import EC2TrafficMirrorFilter


class EC2CreateTrafficMirrorFilterResponse(BaseModel):
    TrafficMirrorFilter: EC2TrafficMirrorFilter | None = None
    ClientToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
