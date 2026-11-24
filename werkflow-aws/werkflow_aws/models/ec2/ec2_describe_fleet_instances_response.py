from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_active_instance import EC2ActiveInstance


class EC2DescribeFleetInstancesResponse(BaseModel):
    ActiveInstances: list[EC2ActiveInstance] | None = None
    NextToken: StrictStr | None = None
    FleetId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
