from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_auto_scaling_auto_scaling_group_availability_zones_list_details import SecurityHubAwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails
from .security_hub_aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification import SecurityHubAwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification
from .security_hub_aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details import SecurityHubAwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails


class SecurityHubAwsAutoScalingAutoScalingGroupDetails(BaseModel):
    LaunchConfigurationName: StrictStr | None = None
    LoadBalancerNames: list[StrictStr] | None = None
    HealthCheckType: StrictStr | None = None
    HealthCheckGracePeriod: StrictInt | None = None
    CreatedTime: StrictStr | None = None
    MixedInstancesPolicy: SecurityHubAwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails | None = None
    AvailabilityZones: list[SecurityHubAwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails] | None = None
    LaunchTemplate: SecurityHubAwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification | None = None
    CapacityRebalance: StrictBool | None = None
