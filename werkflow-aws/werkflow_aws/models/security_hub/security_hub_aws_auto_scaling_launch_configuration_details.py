from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_auto_scaling_launch_configuration_block_device_mappings_details import SecurityHubAwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails
from .security_hub_aws_auto_scaling_launch_configuration_instance_monitoring_details import SecurityHubAwsAutoScalingLaunchConfigurationInstanceMonitoringDetails
from .security_hub_aws_auto_scaling_launch_configuration_metadata_options import SecurityHubAwsAutoScalingLaunchConfigurationMetadataOptions


class SecurityHubAwsAutoScalingLaunchConfigurationDetails(BaseModel):
    AssociatePublicIpAddress: StrictBool | None = None
    BlockDeviceMappings: list[SecurityHubAwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails] | None = None
    ClassicLinkVpcId: StrictStr | None = None
    ClassicLinkVpcSecurityGroups: list[StrictStr] | None = None
    CreatedTime: StrictStr | None = None
    EbsOptimized: StrictBool | None = None
    IamInstanceProfile: StrictStr | None = None
    ImageId: StrictStr | None = None
    InstanceMonitoring: SecurityHubAwsAutoScalingLaunchConfigurationInstanceMonitoringDetails | None = None
    InstanceType: StrictStr | None = None
    KernelId: StrictStr | None = None
    KeyName: StrictStr | None = None
    LaunchConfigurationName: StrictStr | None = None
    PlacementTenancy: StrictStr | None = None
    RamdiskId: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
    SpotPrice: StrictStr | None = None
    UserData: StrictStr | None = None
    MetadataOptions: SecurityHubAwsAutoScalingLaunchConfigurationMetadataOptions | None = None
