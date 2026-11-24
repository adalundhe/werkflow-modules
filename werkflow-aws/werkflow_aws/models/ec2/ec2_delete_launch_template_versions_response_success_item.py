from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2DeleteLaunchTemplateVersionsResponseSuccessItem(BaseModel):
    LaunchTemplateId: StrictStr | None = None
    LaunchTemplateName: StrictStr | None = None
    VersionNumber: StrictInt | None = None
