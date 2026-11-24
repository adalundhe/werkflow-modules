from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_instance_topology import EC2InstanceTopology


class EC2DescribeInstanceTopologyResponse(BaseModel):
    Instances: list[EC2InstanceTopology] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
