from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_instance_status import EC2InstanceStatus


class EC2DescribeInstanceStatusResponse(BaseModel):
    InstanceStatuses: list[EC2InstanceStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
