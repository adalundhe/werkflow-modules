from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_instance_event_window import EC2InstanceEventWindow


class EC2DisassociateInstanceEventWindowResponse(BaseModel):
    InstanceEventWindow: EC2InstanceEventWindow | None = None
    ResponseMetadata: dict[str, Any] | None = None
