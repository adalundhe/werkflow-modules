from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .auto_scaling_availability_zone_distribution import AutoScalingAvailabilityZoneDistribution
from .auto_scaling_availability_zone_impairment_policy import AutoScalingAvailabilityZoneImpairmentPolicy
from .auto_scaling_capacity_reservation_specification import AutoScalingCapacityReservationSpecification
from .auto_scaling_instance_lifecycle_policy import AutoScalingInstanceLifecyclePolicy
from .auto_scaling_instance_maintenance_policy import AutoScalingInstanceMaintenancePolicy
from .auto_scaling_launch_template_specification import AutoScalingLaunchTemplateSpecification
from .auto_scaling_lifecycle_hook_specification import AutoScalingLifecycleHookSpecification
from .auto_scaling_mixed_instances_policy import AutoScalingMixedInstancesPolicy
from .auto_scaling_operator import AutoScalingOperator
from .auto_scaling_tag import AutoScalingTag
from .auto_scaling_traffic_source_identifier import AutoScalingTrafficSourceIdentifier


class AutoScalingCreateAutoScalingGroupRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    MinSize: StrictInt
    MaxSize: StrictInt
    LaunchConfigurationName: StrictStr | None = None
    LaunchTemplate: AutoScalingLaunchTemplateSpecification | None = None
    MixedInstancesPolicy: AutoScalingMixedInstancesPolicy | None = None
    InstanceId: StrictStr | None = None
    DesiredCapacity: StrictInt | None = None
    DefaultCooldown: StrictInt | None = None
    AvailabilityZones: list[StrictStr] | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
    LoadBalancerNames: list[StrictStr] | None = None
    TargetGroupARNs: list[StrictStr] | None = None
    HealthCheckType: StrictStr | None = None
    HealthCheckGracePeriod: StrictInt | None = None
    PlacementGroup: StrictStr | None = None
    VPCZoneIdentifier: StrictStr | None = None
    TerminationPolicies: list[StrictStr] | None = None
    NewInstancesProtectedFromScaleIn: StrictBool | None = None
    CapacityRebalance: StrictBool | None = None
    LifecycleHookSpecificationList: list[AutoScalingLifecycleHookSpecification] | None = None
    DeletionProtection: Literal['none', 'prevent-force-deletion', 'prevent-all-deletion'] | None = None
    Tags: list[AutoScalingTag] | None = None
    ServiceLinkedRoleARN: StrictStr | None = None
    MaxInstanceLifetime: StrictInt | None = None
    Context: StrictStr | None = None
    DesiredCapacityType: StrictStr | None = None
    DefaultInstanceWarmup: StrictInt | None = None
    TrafficSources: list[AutoScalingTrafficSourceIdentifier] | None = None
    InstanceMaintenancePolicy: AutoScalingInstanceMaintenancePolicy | None = None
    AvailabilityZoneDistribution: AutoScalingAvailabilityZoneDistribution | None = None
    AvailabilityZoneImpairmentPolicy: AutoScalingAvailabilityZoneImpairmentPolicy | None = None
    SkipZonalShiftValidation: StrictBool | None = None
    CapacityReservationSpecification: AutoScalingCapacityReservationSpecification | None = None
    InstanceLifecyclePolicy: AutoScalingInstanceLifecyclePolicy | None = None
    Operator: AutoScalingOperator | None = None
