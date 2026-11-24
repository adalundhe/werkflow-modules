from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_instance_event_window_state_change import EC2InstanceEventWindowStateChange


class EC2DeleteInstanceEventWindowResponse(BaseModel):
    InstanceEventWindowState: EC2InstanceEventWindowStateChange | None = None
    ResponseMetadata: dict[str, Any] | None = None
