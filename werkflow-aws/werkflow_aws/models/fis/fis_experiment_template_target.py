from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_experiment_template_target_filter import FISExperimentTemplateTargetFilter


class FISExperimentTemplateTarget(BaseModel):
    resourceType: StrictStr | None = None
    resourceArns: list[StrictStr] | None = None
    resourceTags: dict[StrictStr, StrictStr] | None = None
    filters: list[FISExperimentTemplateTargetFilter] | None = None
    selectionMode: StrictStr | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
