from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .auto_scaling_availability_zone_distribution import AutoScalingAvailabilityZoneDistribution
from .auto_scaling_availability_zone_impairment_policy import AutoScalingAvailabilityZoneImpairmentPolicy
from .auto_scaling_capacity_reservation_specification import AutoScalingCapacityReservationSpecification
from .auto_scaling_enabled_metric import AutoScalingEnabledMetric
from .auto_scaling_instance import AutoScalingInstance
from .auto_scaling_instance_lifecycle_policy import AutoScalingInstanceLifecyclePolicy
from .auto_scaling_instance_maintenance_policy import AutoScalingInstanceMaintenancePolicy
from .auto_scaling_launch_template_specification import AutoScalingLaunchTemplateSpecification
from .auto_scaling_mixed_instances_policy import AutoScalingMixedInstancesPolicy
from .auto_scaling_operator import AutoScalingOperator
from .auto_scaling_suspended_process import AutoScalingSuspendedProcess
from .auto_scaling_tag_description import AutoScalingTagDescription
from .auto_scaling_traffic_source_identifier import AutoScalingTrafficSourceIdentifier
from .auto_scaling_warm_pool_configuration import AutoScalingWarmPoolConfiguration


class AutoScalingGroup(BaseModel):
    AutoScalingGroupName: StrictStr | None = None
    AutoScalingGroupARN: StrictStr | None = None
    LaunchConfigurationName: StrictStr | None = None
    LaunchTemplate: AutoScalingLaunchTemplateSpecification | None = None
    MixedInstancesPolicy: AutoScalingMixedInstancesPolicy | None = None
    MinSize: StrictInt | None = None
    MaxSize: StrictInt | None = None
    DesiredCapacity: StrictInt | None = None
    PredictedCapacity: StrictInt | None = None
    DefaultCooldown: StrictInt | None = None
    AvailabilityZones: list[StrictStr] | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
    LoadBalancerNames: list[StrictStr] | None = None
    TargetGroupARNs: list[StrictStr] | None = None
    HealthCheckType: StrictStr | None = None
    HealthCheckGracePeriod: StrictInt | None = None
    Instances: list[AutoScalingInstance] | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    SuspendedProcesses: list[AutoScalingSuspendedProcess] | None = None
    PlacementGroup: StrictStr | None = None
    VPCZoneIdentifier: StrictStr | None = None
    EnabledMetrics: list[AutoScalingEnabledMetric] | None = None
    Status: StrictStr | None = None
    Tags: list[AutoScalingTagDescription] | None = None
    TerminationPolicies: list[StrictStr] | None = None
    NewInstancesProtectedFromScaleIn: StrictBool | None = None
    ServiceLinkedRoleARN: StrictStr | None = None
    MaxInstanceLifetime: StrictInt | None = None
    CapacityRebalance: StrictBool | None = None
    WarmPoolConfiguration: AutoScalingWarmPoolConfiguration | None = None
    WarmPoolSize: StrictInt | None = None
    Context: StrictStr | None = None
    DesiredCapacityType: StrictStr | None = None
    DefaultInstanceWarmup: StrictInt | None = None
    TrafficSources: list[AutoScalingTrafficSourceIdentifier] | None = None
    InstanceMaintenancePolicy: AutoScalingInstanceMaintenancePolicy | None = None
    DeletionProtection: StrictStr | None = None
    AvailabilityZoneDistribution: AutoScalingAvailabilityZoneDistribution | None = None
    AvailabilityZoneImpairmentPolicy: AutoScalingAvailabilityZoneImpairmentPolicy | None = None
    CapacityReservationSpecification: AutoScalingCapacityReservationSpecification | None = None
    InstanceLifecyclePolicy: AutoScalingInstanceLifecyclePolicy | None = None
    Operator: AutoScalingOperator | None = None
