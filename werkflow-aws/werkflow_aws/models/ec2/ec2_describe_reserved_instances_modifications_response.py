from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_reserved_instances_modification import EC2ReservedInstancesModification


class EC2DescribeReservedInstancesModificationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ReservedInstancesModifications: list[EC2ReservedInstancesModification] | None = None
    ResponseMetadata: dict[str, Any] | None = None
