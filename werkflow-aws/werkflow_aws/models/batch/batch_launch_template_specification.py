from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_launch_template_specification_override import BatchLaunchTemplateSpecificationOverride


class BatchLaunchTemplateSpecification(BaseModel):
    launchTemplateId: StrictStr | None = None
    launchTemplateName: StrictStr | None = None
    version: StrictStr | None = None
    overrides: list[BatchLaunchTemplateSpecificationOverride] | None = None
    userdataType: StrictStr | None = None
