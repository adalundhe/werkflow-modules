from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_experiment_target_filter import FISExperimentTargetFilter


class FISExperimentTarget(BaseModel):
    resourceType: StrictStr | None = None
    resourceArns: list[StrictStr] | None = None
    resourceTags: dict[StrictStr, StrictStr] | None = None
    filters: list[FISExperimentTargetFilter] | None = None
    selectionMode: StrictStr | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
