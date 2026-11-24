from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_capacity_manager_monitored_tag_key import EC2CapacityManagerMonitoredTagKey


class EC2UpdateCapacityManagerMonitoredTagKeysResponse(BaseModel):
    CapacityManagerTagKeys: list[EC2CapacityManagerMonitoredTagKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
