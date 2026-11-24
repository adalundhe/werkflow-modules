from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_hyper_parameter_training_job_summary import SageMakerHyperParameterTrainingJobSummary


class SageMakerListTrainingJobsForHyperParameterTuningJobResponse(BaseModel):
    TrainingJobSummaries: list[SageMakerHyperParameterTrainingJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
