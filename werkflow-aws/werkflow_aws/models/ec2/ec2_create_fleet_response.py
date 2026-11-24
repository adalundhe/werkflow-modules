from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_create_fleet_error import EC2CreateFleetError
from .ec2_create_fleet_instance import EC2CreateFleetInstance


class EC2CreateFleetResponse(BaseModel):
    FleetId: StrictStr | None = None
    Errors: list[EC2CreateFleetError] | None = None
    Instances: list[EC2CreateFleetInstance] | None = None
    ResponseMetadata: dict[str, Any] | None = None
