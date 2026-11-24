from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .auto_scaling_availability_zone_distribution import AutoScalingAvailabilityZoneDistribution
from .auto_scaling_availability_zone_impairment_policy import AutoScalingAvailabilityZoneImpairmentPolicy
from .auto_scaling_capacity_reservation_specification import AutoScalingCapacityReservationSpecification
from .auto_scaling_instance_lifecycle_policy import AutoScalingInstanceLifecyclePolicy
from .auto_scaling_instance_maintenance_policy import AutoScalingInstanceMaintenancePolicy
from .auto_scaling_launch_template_specification import AutoScalingLaunchTemplateSpecification
from .auto_scaling_mixed_instances_policy import AutoScalingMixedInstancesPolicy


class AutoScalingUpdateAutoScalingGroupRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    LaunchConfigurationName: StrictStr | None = None
    LaunchTemplate: AutoScalingLaunchTemplateSpecification | None = None
    MixedInstancesPolicy: AutoScalingMixedInstancesPolicy | None = None
    MinSize: StrictInt | None = None
    MaxSize: StrictInt | None = None
    DesiredCapacity: StrictInt | None = None
    DefaultCooldown: StrictInt | None = None
    AvailabilityZones: list[StrictStr] | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
    HealthCheckType: StrictStr | None = None
    HealthCheckGracePeriod: StrictInt | None = None
    PlacementGroup: StrictStr | None = None
    VPCZoneIdentifier: StrictStr | None = None
    TerminationPolicies: list[StrictStr] | None = None
    NewInstancesProtectedFromScaleIn: StrictBool | None = None
    ServiceLinkedRoleARN: StrictStr | None = None
    MaxInstanceLifetime: StrictInt | None = None
    CapacityRebalance: StrictBool | None = None
    Context: StrictStr | None = None
    DesiredCapacityType: StrictStr | None = None
    DefaultInstanceWarmup: StrictInt | None = None
    InstanceMaintenancePolicy: AutoScalingInstanceMaintenancePolicy | None = None
    AvailabilityZoneDistribution: AutoScalingAvailabilityZoneDistribution | None = None
    AvailabilityZoneImpairmentPolicy: AutoScalingAvailabilityZoneImpairmentPolicy | None = None
    SkipZonalShiftValidation: StrictBool | None = None
    CapacityReservationSpecification: AutoScalingCapacityReservationSpecification | None = None
    InstanceLifecyclePolicy: AutoScalingInstanceLifecyclePolicy | None = None
    DeletionProtection: Literal['none', 'prevent-force-deletion', 'prevent-all-deletion'] | None = None
