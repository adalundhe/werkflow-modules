from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchLaunchTemplateSpecificationOverride(BaseModel):
    launchTemplateId: StrictStr | None = None
    launchTemplateName: StrictStr | None = None
    version: StrictStr | None = None
    targetInstanceTypes: list[StrictStr] | None = None
    userdataType: StrictStr | None = None
