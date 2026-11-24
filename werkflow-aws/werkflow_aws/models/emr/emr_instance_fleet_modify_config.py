from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_instance_fleet_resizing_specifications import EMRInstanceFleetResizingSpecifications
from .emr_instance_type_config import EMRInstanceTypeConfig


class EMRInstanceFleetModifyConfig(BaseModel):
    InstanceFleetId: StrictStr
    TargetOnDemandCapacity: StrictInt | None = None
    TargetSpotCapacity: StrictInt | None = None
    ResizeSpecifications: EMRInstanceFleetResizingSpecifications | None = None
    InstanceTypeConfigs: list[EMRInstanceTypeConfig] | None = None
    Context: StrictStr | None = None
