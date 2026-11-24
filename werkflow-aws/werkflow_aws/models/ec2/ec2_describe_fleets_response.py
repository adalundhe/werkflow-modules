from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_fleet_data import EC2FleetData


class EC2DescribeFleetsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Fleets: list[EC2FleetData] | None = None
    ResponseMetadata: dict[str, Any] | None = None
