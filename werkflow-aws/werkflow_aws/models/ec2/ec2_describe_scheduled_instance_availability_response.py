from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_scheduled_instance_availability import EC2ScheduledInstanceAvailability


class EC2DescribeScheduledInstanceAvailabilityResponse(BaseModel):
    NextToken: StrictStr | None = None
    ScheduledInstanceAvailabilitySet: list[EC2ScheduledInstanceAvailability] | None = None
    ResponseMetadata: dict[str, Any] | None = None
