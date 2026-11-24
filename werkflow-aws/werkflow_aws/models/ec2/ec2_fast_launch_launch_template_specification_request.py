from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2FastLaunchLaunchTemplateSpecificationRequest(BaseModel):
    Version: StrictStr
    LaunchTemplateId: StrictStr | None = None
    LaunchTemplateName: StrictStr | None = None
