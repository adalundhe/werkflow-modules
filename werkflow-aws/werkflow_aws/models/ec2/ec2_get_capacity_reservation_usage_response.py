from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_instance_usage import EC2InstanceUsage
from .ec2_interruptible_capacity_allocation import EC2InterruptibleCapacityAllocation
from .ec2_interruption_info import EC2InterruptionInfo


class EC2GetCapacityReservationUsageResponse(BaseModel):
    NextToken: StrictStr | None = None
    CapacityReservationId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    AvailableInstanceCount: StrictInt | None = None
    State: StrictStr | None = None
    InstanceUsages: list[EC2InstanceUsage] | None = None
    Interruptible: StrictBool | None = None
    InterruptibleCapacityAllocation: EC2InterruptibleCapacityAllocation | None = None
    InterruptionInfo: EC2InterruptionInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
