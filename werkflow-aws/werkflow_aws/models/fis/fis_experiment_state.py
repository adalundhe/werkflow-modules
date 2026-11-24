from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_experiment_error import FISExperimentError


class FISExperimentState(BaseModel):
    status: StrictStr | None = None
    reason: StrictStr | None = None
    error: FISExperimentError | None = None
