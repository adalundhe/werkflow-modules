from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_auto_scaling_launch_configuration_block_device_mappings_ebs_details import SecurityHubAwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails


class SecurityHubAwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails(BaseModel):
    DeviceName: StrictStr | None = None
    Ebs: SecurityHubAwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails | None = None
    NoDevice: StrictBool | None = None
    VirtualName: StrictStr | None = None
