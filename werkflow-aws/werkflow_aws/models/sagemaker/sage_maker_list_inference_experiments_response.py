from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_experiment_summary import SageMakerInferenceExperimentSummary


class SageMakerListInferenceExperimentsResponse(BaseModel):
    InferenceExperiments: list[SageMakerInferenceExperimentSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
