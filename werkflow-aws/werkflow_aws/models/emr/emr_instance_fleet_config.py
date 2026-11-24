from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_instance_fleet_provisioning_specifications import EMRInstanceFleetProvisioningSpecifications
from .emr_instance_fleet_resizing_specifications import EMRInstanceFleetResizingSpecifications
from .emr_instance_type_config import EMRInstanceTypeConfig


class EMRInstanceFleetConfig(BaseModel):
    InstanceFleetType: Literal['MASTER', 'CORE', 'TASK']
    Name: StrictStr | None = None
    TargetOnDemandCapacity: StrictInt | None = None
    TargetSpotCapacity: StrictInt | None = None
    InstanceTypeConfigs: list[EMRInstanceTypeConfig] | None = None
    LaunchSpecifications: EMRInstanceFleetProvisioningSpecifications | None = None
    ResizeSpecifications: EMRInstanceFleetResizingSpecifications | None = None
    Context: StrictStr | None = None
