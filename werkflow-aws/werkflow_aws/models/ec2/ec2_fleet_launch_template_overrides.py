from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ec2_block_device_mapping_response import EC2BlockDeviceMappingResponse
from .ec2_instance_requirements import EC2InstanceRequirements
from .ec2_placement_response import EC2PlacementResponse


class EC2FleetLaunchTemplateOverrides(BaseModel):
    InstanceType: StrictStr | None = None
    MaxPrice: StrictStr | None = None
    SubnetId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    WeightedCapacity: StrictFloat | StrictInt | None = None
    Priority: StrictFloat | StrictInt | None = None
    Placement: EC2PlacementResponse | None = None
    InstanceRequirements: EC2InstanceRequirements | None = None
    ImageId: StrictStr | None = None
    BlockDeviceMappings: list[EC2BlockDeviceMappingResponse] | None = None
    AvailabilityZoneId: StrictStr | None = None
