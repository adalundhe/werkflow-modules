from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_launch_template_and_overrides_response import EC2LaunchTemplateAndOverridesResponse


class EC2DescribeFleetsInstances(BaseModel):
    LaunchTemplateAndOverrides: EC2LaunchTemplateAndOverridesResponse | None = None
    Lifecycle: StrictStr | None = None
    InstanceIds: list[StrictStr] | None = None
    InstanceType: StrictStr | None = None
    Platform: StrictStr | None = None
