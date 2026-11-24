from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_start_experiment_experiment_options_input import FISStartExperimentExperimentOptionsInput


class FISStartExperimentRequest(BaseModel):
    clientToken: StrictStr
    experimentTemplateId: StrictStr
    experimentOptions: FISStartExperimentExperimentOptionsInput | None = None
    tags: dict[StrictStr, StrictStr] | None = None
