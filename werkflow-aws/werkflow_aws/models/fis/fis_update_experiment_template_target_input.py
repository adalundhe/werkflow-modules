from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_experiment_template_target_input_filter import FISExperimentTemplateTargetInputFilter


class FISUpdateExperimentTemplateTargetInput(BaseModel):
    resourceType: StrictStr
    selectionMode: StrictStr
    resourceArns: list[StrictStr] | None = None
    resourceTags: dict[StrictStr, StrictStr] | None = None
    filters: list[FISExperimentTemplateTargetInputFilter] | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
