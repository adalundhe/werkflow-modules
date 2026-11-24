from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_availability_zone import EC2AvailabilityZone


class EC2DescribeAvailabilityZonesResponse(BaseModel):
    AvailabilityZones: list[EC2AvailabilityZone] | None = None
    ResponseMetadata: dict[str, Any] | None = None
