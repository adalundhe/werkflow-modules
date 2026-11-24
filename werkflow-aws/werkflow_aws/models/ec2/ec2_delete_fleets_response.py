from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_delete_fleet_error_item import EC2DeleteFleetErrorItem
from .ec2_delete_fleet_success_item import EC2DeleteFleetSuccessItem


class EC2DeleteFleetsResponse(BaseModel):
    SuccessfulFleetDeletions: list[EC2DeleteFleetSuccessItem] | None = None
    UnsuccessfulFleetDeletions: list[EC2DeleteFleetErrorItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
