from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_delete_fleet_error import EC2DeleteFleetError


class EC2DeleteFleetErrorItem(BaseModel):
    Error: EC2DeleteFleetError | None = None
    FleetId: StrictStr | None = None
