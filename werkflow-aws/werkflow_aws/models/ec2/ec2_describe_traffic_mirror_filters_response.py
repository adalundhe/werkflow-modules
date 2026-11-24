from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_traffic_mirror_filter import EC2TrafficMirrorFilter


class EC2DescribeTrafficMirrorFiltersResponse(BaseModel):
    TrafficMirrorFilters: list[EC2TrafficMirrorFilter] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
