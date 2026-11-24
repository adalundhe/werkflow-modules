from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_instance_monitoring import EC2InstanceMonitoring


class EC2UnmonitorInstancesResponse(BaseModel):
    InstanceMonitorings: list[EC2InstanceMonitoring] | None = None
    ResponseMetadata: dict[str, Any] | None = None
