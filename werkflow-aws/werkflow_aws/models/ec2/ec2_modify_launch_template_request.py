from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyLaunchTemplateRequest(BaseModel):
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
    LaunchTemplateId: StrictStr | None = None
    LaunchTemplateName: StrictStr | None = None
    DefaultVersion: StrictStr | None = None
