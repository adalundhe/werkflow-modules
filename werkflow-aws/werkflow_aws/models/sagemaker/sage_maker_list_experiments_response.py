from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_experiment_summary import SageMakerExperimentSummary


class SageMakerListExperimentsResponse(BaseModel):
    ExperimentSummaries: list[SageMakerExperimentSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
