from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_instance_event_window import EC2InstanceEventWindow


class EC2DescribeInstanceEventWindowsResponse(BaseModel):
    InstanceEventWindows: list[EC2InstanceEventWindow] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
