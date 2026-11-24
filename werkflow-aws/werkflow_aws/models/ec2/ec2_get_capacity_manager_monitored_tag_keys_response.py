from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_manager_monitored_tag_key import EC2CapacityManagerMonitoredTagKey


class EC2GetCapacityManagerMonitoredTagKeysResponse(BaseModel):
    CapacityManagerTagKeys: list[EC2CapacityManagerMonitoredTagKey] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
