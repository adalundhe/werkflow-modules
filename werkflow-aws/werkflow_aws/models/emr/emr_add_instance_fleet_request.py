from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_instance_fleet_config import EMRInstanceFleetConfig


class EMRAddInstanceFleetRequest(BaseModel):
    ClusterId: StrictStr
    InstanceFleet: EMRInstanceFleetConfig
