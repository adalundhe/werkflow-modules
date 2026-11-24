from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_fast_launch_launch_template_specification_request import EC2FastLaunchLaunchTemplateSpecificationRequest
from .ec2_fast_launch_snapshot_configuration_request import EC2FastLaunchSnapshotConfigurationRequest


class EC2EnableFastLaunchRequest(BaseModel):
    ImageId: StrictStr
    ResourceType: StrictStr | None = None
    SnapshotConfiguration: EC2FastLaunchSnapshotConfigurationRequest | None = None
    LaunchTemplate: EC2FastLaunchLaunchTemplateSpecificationRequest | None = None
    MaxParallelLaunches: StrictInt | None = None
    DryRun: StrictBool | None = None
