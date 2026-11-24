from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteLaunchTemplateVersionsRequest(BaseModel):
    Versions: list[StrictStr]
    DryRun: StrictBool | None = None
    LaunchTemplateId: StrictStr | None = None
    LaunchTemplateName: StrictStr | None = None
