from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .fis_experiment_options import FISExperimentOptions
from .fis_experiment_state import FISExperimentState


class FISExperimentSummary(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    experimentTemplateId: StrictStr | None = None
    state: FISExperimentState | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    experimentOptions: FISExperimentOptions | None = None
