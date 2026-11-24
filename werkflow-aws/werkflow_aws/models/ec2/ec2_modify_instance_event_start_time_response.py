from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_instance_status_event import EC2InstanceStatusEvent


class EC2ModifyInstanceEventStartTimeResponse(BaseModel):
    Event: EC2InstanceStatusEvent | None = None
    ResponseMetadata: dict[str, Any] | None = None
