from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_scheduled_instance import EC2ScheduledInstance


class EC2PurchaseScheduledInstancesResponse(BaseModel):
    ScheduledInstanceSet: list[EC2ScheduledInstance] | None = None
    ResponseMetadata: dict[str, Any] | None = None
