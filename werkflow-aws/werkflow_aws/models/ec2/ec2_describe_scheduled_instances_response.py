from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_scheduled_instance import EC2ScheduledInstance


class EC2DescribeScheduledInstancesResponse(BaseModel):
    NextToken: StrictStr | None = None
    ScheduledInstanceSet: list[EC2ScheduledInstance] | None = None
    ResponseMetadata: dict[str, Any] | None = None
