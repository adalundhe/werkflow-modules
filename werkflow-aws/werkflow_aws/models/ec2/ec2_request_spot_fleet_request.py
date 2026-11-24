from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_spot_fleet_request_config_data import EC2SpotFleetRequestConfigData


class EC2RequestSpotFleetRequest(BaseModel):
    SpotFleetRequestConfig: EC2SpotFleetRequestConfigData
    DryRun: StrictBool | None = None
