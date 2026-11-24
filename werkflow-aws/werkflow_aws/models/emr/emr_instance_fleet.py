from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_instance_fleet_provisioning_specifications import EMRInstanceFleetProvisioningSpecifications
from .emr_instance_fleet_resizing_specifications import EMRInstanceFleetResizingSpecifications
from .emr_instance_fleet_status import EMRInstanceFleetStatus
from .emr_instance_type_specification import EMRInstanceTypeSpecification


class EMRInstanceFleet(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Status: EMRInstanceFleetStatus | None = None
    InstanceFleetType: StrictStr | None = None
    TargetOnDemandCapacity: StrictInt | None = None
    TargetSpotCapacity: StrictInt | None = None
    ProvisionedOnDemandCapacity: StrictInt | None = None
    ProvisionedSpotCapacity: StrictInt | None = None
    InstanceTypeSpecifications: list[EMRInstanceTypeSpecification] | None = None
    LaunchSpecifications: EMRInstanceFleetProvisioningSpecifications | None = None
    ResizeSpecifications: EMRInstanceFleetResizingSpecifications | None = None
    Context: StrictStr | None = None
