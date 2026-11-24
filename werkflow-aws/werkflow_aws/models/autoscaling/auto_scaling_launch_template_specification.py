from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingLaunchTemplateSpecification(BaseModel):
    LaunchTemplateId: StrictStr | None = None
    LaunchTemplateName: StrictStr | None = None
    Version: StrictStr | None = None
