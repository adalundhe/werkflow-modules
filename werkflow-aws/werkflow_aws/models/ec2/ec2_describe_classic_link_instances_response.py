from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_classic_link_instance import EC2ClassicLinkInstance


class EC2DescribeClassicLinkInstancesResponse(BaseModel):
    Instances: list[EC2ClassicLinkInstance] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
