from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .auto_scaling_block_device_mapping import AutoScalingBlockDeviceMapping
from .auto_scaling_instance_metadata_options import AutoScalingInstanceMetadataOptions
from .auto_scaling_instance_monitoring import AutoScalingInstanceMonitoring


class AutoScalingCreateLaunchConfigurationRequest(BaseModel):
    LaunchConfigurationName: StrictStr
    ImageId: StrictStr | None = None
    KeyName: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
    ClassicLinkVPCId: StrictStr | None = None
    ClassicLinkVPCSecurityGroups: list[StrictStr] | None = None
    UserData: StrictStr | None = None
    InstanceId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    KernelId: StrictStr | None = None
    RamdiskId: StrictStr | None = None
    BlockDeviceMappings: list[AutoScalingBlockDeviceMapping] | None = None
    InstanceMonitoring: AutoScalingInstanceMonitoring | None = None
    SpotPrice: StrictStr | None = None
    IamInstanceProfile: StrictStr | None = None
    EbsOptimized: StrictBool | None = None
    AssociatePublicIpAddress: StrictBool | None = None
    PlacementTenancy: StrictStr | None = None
    MetadataOptions: AutoScalingInstanceMetadataOptions | None = None
