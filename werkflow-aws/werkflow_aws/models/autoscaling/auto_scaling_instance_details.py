from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .auto_scaling_launch_template_specification import AutoScalingLaunchTemplateSpecification


class AutoScalingInstanceDetails(BaseModel):
    InstanceId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    AutoScalingGroupName: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    LifecycleState: StrictStr | None = None
    HealthStatus: StrictStr | None = None
    LaunchConfigurationName: StrictStr | None = None
    LaunchTemplate: AutoScalingLaunchTemplateSpecification | None = None
    ImageId: StrictStr | None = None
    ProtectedFromScaleIn: StrictBool | None = None
    WeightedCapacity: StrictStr | None = None
