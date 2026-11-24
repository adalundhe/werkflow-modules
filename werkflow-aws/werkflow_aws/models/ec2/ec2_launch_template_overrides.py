from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ec2_instance_requirements import EC2InstanceRequirements


class EC2LaunchTemplateOverrides(BaseModel):
    InstanceType: StrictStr | None = None
    SpotPrice: StrictStr | None = None
    SubnetId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    WeightedCapacity: StrictFloat | StrictInt | None = None
    Priority: StrictFloat | StrictInt | None = None
    InstanceRequirements: EC2InstanceRequirements | None = None
    AvailabilityZoneId: StrictStr | None = None
