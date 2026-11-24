from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_fast_launch_launch_template_specification_response import EC2FastLaunchLaunchTemplateSpecificationResponse
from .ec2_fast_launch_snapshot_configuration_response import EC2FastLaunchSnapshotConfigurationResponse


class EC2DisableFastLaunchResponse(BaseModel):
    ImageId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    SnapshotConfiguration: EC2FastLaunchSnapshotConfigurationResponse | None = None
    LaunchTemplate: EC2FastLaunchLaunchTemplateSpecificationResponse | None = None
    MaxParallelLaunches: StrictInt | None = None
    OwnerId: StrictStr | None = None
    State: StrictStr | None = None
    StateTransitionReason: StrictStr | None = None
    StateTransitionTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
