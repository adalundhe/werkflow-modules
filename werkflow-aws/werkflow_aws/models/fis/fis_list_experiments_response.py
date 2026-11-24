from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fis_experiment_summary import FISExperimentSummary


class FISListExperimentsResponse(BaseModel):
    experiments: list[FISExperimentSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
