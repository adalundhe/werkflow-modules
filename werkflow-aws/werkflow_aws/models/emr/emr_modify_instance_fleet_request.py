from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_instance_fleet_modify_config import EMRInstanceFleetModifyConfig


class EMRModifyInstanceFleetRequest(BaseModel):
    ClusterId: StrictStr
    InstanceFleet: EMRInstanceFleetModifyConfig
